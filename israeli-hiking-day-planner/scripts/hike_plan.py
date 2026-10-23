#!/usr/bin/env python3
"""Offline day-hike planner for Israel: heat bands, timing window, water, route card.

No network access. The agent fetches the data (IMS hourly heat stress, IMS
warnings, sunset, route distance/ascent, site hours, the site's published walking
time) and passes it in; this script only applies the rules and formats a Markdown
route card. Every rule it applies is listed in the skill's evidence.json.

Exit codes: 0 = no NO-GO condition found, 1 = NO-GO, 2 = bad input or script error.

Example (Ein Gedi IMS forecast for 2026-10-23 applied to INPA's winter weekday hours, Hidden Waterfall, INPA 3-4 h, upper end):
  python3 scripts/hike_plan.py --name "Nahal Arugot, Hidden Waterfall" \
    --date 2026-10-23 --checked-at "2026-10-23 07:00" \
    --distance-km 4 --ascent-m 150 --duration-h 4 --region south \
    --heat "08:23.0,09:23.7,10:24.6,11:25.6,12:26.4,13:27.2,14:27.8,15:28.4,16:27.9" \
    --sunset 17:58 --opens 08:00 --last-entry 13:00 --last-exit 14:30 \
    --site-water-l 3 --ages 40,38,9,7 --start 08:00 --warning yellow \
    --checked inpa,hfc,firing,ims,flood --wadi
"""
import argparse
import datetime
import math
import sys

# IMS heat-stress scale (discomfort index, units). Classify from the NUMERIC
# heat_stress value; the API's integer heat_stress_level does not match it.
HEAT_BANDS = [
    (30.0, "extreme", "קיצוני"),
    (28.0, "heavy", "כבד"),
    (26.0, "moderate", "בינוני"),
    (24.0, "mild", "מתון"),
    (22.0, "light", "קל"),
]
BAND_ORDER = ["none", "light", "mild", "moderate", "heavy", "extreme"]

# INPA public guidance: litres per person by region.
INPA_REGION_WATER_L = {"north": 3.0, "south": 5.0}
# Ministry of Education 2016 school-trip minimum on foot (litres per day).
# The circular names three day types but does not map them to IMS bands. This
# skill's reading: no heat stress = regular day, light or mild = hot day,
# moderate and above = heat load.
MOE_DAILY_MIN_L = {"regular": 1.5, "hot": 3.0, "heat_load": 4.5}
# Ministry of Education heat-load card, litres per walking hour, school ages.
MOE_PER_HOUR_BY_AGE = [((6, 10), 0.5), ((11, 18), 0.75)]

FINISH_BEFORE_DARK_MIN = 60  # MoE: end a walking trip about an hour before dark
CHECKS = {
    "inpa": "INPA closed trails and newsflashes",
    "hfc": "Home Front Command policy for the zone",
    "firing": "IDF firing zones and closed military areas",
    "ims": "IMS warnings",
    "flood": "flood check: rain over the catchment today and the previous day",
}


def band_of(value):
    for threshold, en, he in HEAT_BANDS:
        if value >= threshold:
            return en, he
    return "none", "אין"


def hm_to_min(s):
    h, m = s.strip().split(":")
    h, m = int(h), int(m)
    if not (0 <= h <= 23 and 0 <= m <= 59):
        raise ValueError(f"time out of range: {s}")
    return h * 60 + m


def min_to_hm(m):
    m = int(round(m))
    if m < 0 or m >= 24 * 60:
        return "--:--"
    return f"{m // 60:02d}:{m % 60:02d}"


def parse_heat(s):
    out = {}
    if not s:
        return out
    for part in s.split(","):
        hour, val = part.strip().split(":", 1)
        if not 0 <= int(hour) <= 23:
            raise ValueError(f"heat hour out of range: {hour}")
        v = float(val)
        if not math.isfinite(v):
            raise ValueError(f"heat value is not a number: {val}")
        out[int(hour)] = v
    return out


def walking_minutes(distance_km, ascent_m):
    # 5 km/h plus one minute per 10 m of ascent (metric Naismith rule). A minimum.
    return distance_km / 5.0 * 60.0 + ascent_m / 10.0


def build(a):
    for name in ("distance_km", "ascent_m", "duration_h", "break_min_per_hour", "site_water_l"):
        v = getattr(a, name)
        if v is not None and v < 0:
            raise ValueError(f"--{name.replace('_', '-')} must not be negative")
    hike_day = datetime.date.fromisoformat(a.date) if a.date else None
    if hike_day and hike_day.weekday() in (4, 5):
        a.weekend = True  # Friday or Saturday; holidays must still be passed with --weekend
    rule_walk = walking_minutes(a.distance_km, a.ascent_m)
    walk = max(rule_walk, a.duration_h * 60.0) if a.duration_h else rule_walk
    total = walk * (1 + a.break_min_per_hour / 60.0)

    ages = [int(x) for x in a.ages.split(",") if x.strip()]
    if any(x < 0 for x in ages):
        raise ValueError("ages must not be negative")
    young = [x for x in ages if x < 10]

    dark_limit = hm_to_min(a.sunset) - FINISH_BEFORE_DARK_MIN
    limits = [("an hour before sunset", dark_limit)]
    if a.last_exit:
        limits.append(("site exit time", hm_to_min(a.last_exit)))
    finish_by_label, finish_by = min(limits, key=lambda x: x[1])
    latest_start = finish_by - total
    if a.last_entry:
        latest_start = min(latest_start, hm_to_min(a.last_entry))
    opens = hm_to_min(a.opens) if a.opens else None

    flags, nogo = [], []
    if a.start:
        start = hm_to_min(a.start)
        if opens is not None and start < opens:
            flags.append(f"Planned start is before the site opens; timing uses the opening time {min_to_hm(opens)}.")
            start = opens
    else:
        start = opens if opens is not None else latest_start
    if opens is not None and opens > latest_start:
        nogo.append(f"No start inside opening hours fits: the site opens {min_to_hm(opens)} but the latest safe start is {min_to_hm(latest_start)}.")
    if start > latest_start:
        nogo.append(f"Start {min_to_hm(start)} is after the latest safe start {min_to_hm(latest_start)}.")
    finish = start + total

    heat = parse_heat(a.heat)
    first_h, last_h = int(start // 60), int(math.ceil(finish / 60.0))
    window = [(h, heat[h]) + band_of(heat[h]) for h in sorted(heat) if first_h <= h <= last_h]
    worst = max((w[2] for w in window), key=BAND_ORDER.index, default="none")
    day_worst = max((band_of(v)[0] for v in heat.values()), key=BAND_ORDER.index, default="none")

    if a.firing_unsure:
        if a.weekend:
            nogo.append("Unclear whether the route crosses a firing zone, on a Friday, Shabbat or holiday when coordination is no longer possible.")
        else:
            flags.append("Unclear whether the route crosses a firing zone: confirm with the regional command's coordination office before going.")
    if a.heatwave:
        nogo.append("IMS heat-wave warning for the area: INPA says hiking is forbidden on sharav days.")
    if a.upstream_rain:
        if a.wadi:
            nogo.append("Rain over the catchment on the hike day or the day before, observed or forecast, on a wadi or canyon route: flood risk even if the trail is dry.")
        else:
            flags.append("Rain over the catchment on the hike day or the day before, observed or forecast: keep out of stream beds and do not cross flowing water.")
    if hike_day and a.checked_at:
        checked_day = datetime.date.fromisoformat(a.checked_at.strip()[:10])
        if checked_day < hike_day:
            flags.append("Checks were done before the hike day: re-check the forecast, warnings and closures on the morning of the hike.")
    if a.sunrise and hm_to_min(a.sunrise) > start and (opens is None or opens > start):
        flags.append(f"Start {min_to_hm(start)} is before sunrise {a.sunrise}: INPA forbids walking in the dark, so start before sunrise only where the site itself opens before sunrise (like the Masada Snake Path).")
    if a.weekend and "firing" not in {c.strip() for c in a.checked.split(",")}:
        nogo.append("Friday, Shabbat or holiday hike without a completed firing-zone check: coordination is no longer possible.")
    if a.wadi and "flood" not in {c.strip() for c in a.checked.split(",")}:
        nogo.append("Wadi or canyon route without a completed flood check (rain over the catchment today and the previous day).")
    if a.judea_samaria:
        flags.append("Route in Judea and Samaria: this skill does not assess security conditions there; check the Home Front Command zone and current notices.")
    if a.closed:
        nogo.append("Route is closed or restricted (INPA list, Home Front Command, closed military area, or a firing zone without confirmed coordination).")
    if a.flood_warning:
        nogo.append("Flood risk: IMS flood, flooding or thunderstorm warning, or rain upstream. Do not enter wadis, canyons or exposed summits.")
    if a.warning in ("orange", "red"):
        nogo.append(f"IMS {a.warning} warning covers the hike area.")
    elif a.warning == "yellow":
        flags.append("IMS yellow warning covers the hike area: read its hours and type before going.")
    if a.fire_danger:
        flags.append("IMS fire-danger warning: no fire of any kind, and check for closures.")
    if a.mine_area:
        flags.append("Mine-danger area: stay on the marked trail, never cross a fence or a yellow-sign / red-triangle boundary.")
    if worst in ("heavy", "extreme"):
        nogo.append(f"Heat stress reaches {worst} during the hike hours. Start earlier, shorten the route, or pick another day.")
    elif worst == "moderate":
        if young and a.region == "south":
            nogo.append("Moderate heat stress inside the hike window with children under 10 in the south (this skill's conservative rule). Finish before the first moderate hour or pick a shorter route.")
        else:
            flags.append("Moderate heat stress inside the hike window: finish before it, keep to shade, avoid exertion 10:00-16:00.")
    if day_worst in ("heavy", "extreme") and worst not in ("heavy", "extreme"):
        flags.append(f"Heat reaches {day_worst} later the same day: keep a margin, and INPA advises giving up the hike on sharav days.")
    if not heat:
        flags.append("No hourly heat data supplied: check the IMS forecast before deciding.")
    else:
        missing = [h for h in range(first_h, last_h + 1) if h not in heat]
        if missing:
            flags.append("No IMS heat value for hour(s) " + ", ".join(f"{h:02d}:00" for h in missing)
                         + " of the hike: the heat check is incomplete.")
    if not a.duration_h:
        flags.append("Walking time is a minimum estimate from distance and ascent. Confirm it with the site's INPA page or the INPA information line *3639, then re-run with --duration-h.")
    done = {c.strip() for c in a.checked.split(",") if c.strip()}
    not_done = [label for key, label in CHECKS.items() if key not in done]
    if not_done:
        flags.append("Not checked yet: " + "; ".join(not_done) + ".")
    if any(x < 6 for x in ages):
        flags.append("Children under 6 in the group: the Ministry of Education water rates below cover ages 6-18 only.")

    day_type = "regular" if worst == "none" else ("hot" if worst in ("light", "mild") else "heat_load")
    candidates = [
        (INPA_REGION_WATER_L[a.region], f"INPA {a.region} guideline"),
        (MOE_DAILY_MIN_L[day_type], f"Ministry of Education minimum, {day_type.replace('_', ' ')} day (school rule)"),
    ]
    if a.site_water_l is not None:
        candidates.append((a.site_water_l, "INPA figure for this site"))
    water_l, water_src = max(candidates, key=lambda c: c[0])

    kid_lines = []
    for age in ages:
        for (lo, hi), rate in MOE_PER_HOUR_BY_AGE:
            if lo <= age <= hi:
                need = rate * walk / 60.0
                pack = max(water_l, need)
                kid_lines.append(f"age {age}: pack at least {pack:.1f} L, drink about {rate} L per walking hour")

    verdict = "NO-GO" if nogo else ("CAUTION" if flags else "NO OFFICIAL WARNING FOUND")
    out = [f"# Route card: {a.name}", ""]
    out.append(f"Hike date: {a.date or 'not given'} | checks done at: {a.checked_at or 'not given'}")
    out.append("")
    if a.organized:
        out.append("This card is not the Ministry of Education's trip approval. A school or youth-movement trip needs that approval and coordination through the trips situation room (02-6222211).")
        out.append("")
    out.append(f"**Decision: {verdict}** (this is not a safety guarantee; official closures and warnings override it)")
    out += ["", "| Item | Value |", "|---|---|"]
    out.append(f"| Distance / ascent | {a.distance_km:g} km / {a.ascent_m:g} m |")
    out.append(f"| Walking-time rule (minimum) | {rule_walk / 60:.1f} h (5 km/h + 1 min per 10 m ascent, no breaks) |")
    if a.duration_h:
        out.append(f"| Published / confirmed duration | {a.duration_h:g} h |")
    if a.break_min_per_hour:
        out.append(f"| With your breaks | {total / 60:.1f} h |")
    out.append(f"| Planned start / finish | {min_to_hm(start)} / {min_to_hm(finish)} |")
    out.append(f"| Finish no later than | {min_to_hm(finish_by)} ({finish_by_label}) |")
    basis = "" if a.duration_h else " (from the minimum walking-time rule, not reliable)"
    out.append(f"| Latest safe start | {min_to_hm(latest_start)}{basis} |")
    kids_more = any(max(water_l, r * walk / 60.0) > water_l for age in ages for (lo, hi), r in MOE_PER_HOUR_BY_AGE if lo <= age <= hi)
    out.append(f"| Water per person | at least {water_l:g} L ({water_src}){'; children need more, see below' if kids_more else ''} |")
    out.append(f"| Worst heat stress in window | {worst} |")
    out.append("")
    if window:
        out += ["| Hour | IMS heat index | Band |", "|---|---|---|"]
        for hour, val, en, he in window:
            out.append(f"| {hour:02d}:00 | {val:.2f} | {en} ({he}) |")
        out.append("")
    if kid_lines:
        out.append("Children (Ministry of Education school guideline): " + "; ".join(kid_lines))
        out.append("")
    out += [f"- NO-GO: {x}" for x in nogo] + [f"- CAUTION: {x}" for x in flags]
    out += ["", "## Equipment",
            "- Water as above and enough food, suitable clothing, walking shoes (closed shoes where INPA requires them), sunscreen, a head cover.",
            "- A mobile phone with a charged battery, and a flashlight or headlamp.",
            "", "## Emergency plan",
            "- Medical emergency (heat illness, a fall, a bite): MDA 101. Distress, a lost hiker, or a rescue: police 100. INPA also lists ZAKA 1220.",
            "- Tell them: exact location, what happened, what help you need.",
            "- Heat-illness signs (headache, weakness, nausea, vomiting, dizziness, confusion): stop, move to shade off the hot ground, call 101.",
            "- Unexploded ordnance or a suspicious object: do not touch or approach it, move away, call 100.",
            "- Caught by dark: stop, stay on the trail, call for help. Anyone separated from the group sits and waits.",
            "- Before leaving: leave a written note (names, phone, route, group size, schedule) on the car window or at the INPA site, and tell someone at home."]
    return "\n".join(out), (1 if nogo else 0)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--name", default="Day hike")
    p.add_argument("--date", help="hike date YYYY-MM-DD (printed on the card)")
    p.add_argument("--checked-at", help="when the checks were done (printed on the card)")
    p.add_argument("--distance-km", type=float, required=True)
    p.add_argument("--ascent-m", type=float, default=0.0)
    p.add_argument("--duration-h", type=float,
                   help="published or user-confirmed round-trip duration; the longer of this and the rule is used")
    p.add_argument("--region", choices=["north", "south"], required=True,
                   help="INPA water region: north (3 L) or south (5 L)")
    p.add_argument("--heat", default="", help="hourly IMS heat_stress values, e.g. '08:23.0,09:23.7'")
    p.add_argument("--sunset", required=True, help="HH:MM local time")
    p.add_argument("--opens", help="site opening HH:MM")
    p.add_argument("--sunrise", help="sunrise HH:MM local time")
    p.add_argument("--last-entry", help="site last entry HH:MM")
    p.add_argument("--last-exit", help="time you must be out HH:MM (use the earliest exit that applies to your route)")
    p.add_argument("--start", help="planned start HH:MM")
    p.add_argument("--break-min-per-hour", type=float, default=0.0,
                   help="your own rest allowance; the walking-time rule excludes breaks")
    p.add_argument("--site-water-l", type=float, help="site-specific INPA water figure per person, if published")
    p.add_argument("--ages", default="", help="comma-separated ages of the group")
    p.add_argument("--warning", choices=["none", "yellow", "orange", "red"], default="none",
                   help="highest non-flood IMS warning covering the hike area")
    p.add_argument("--flood-warning", action="store_true",
                   help="IMS flood, flooding or thunderstorm warning covering the route (wadi, canyon or exposed summit)")
    p.add_argument("--fire-danger", action="store_true", help="IMS fire-danger warning for the area")
    p.add_argument("--mine-area", action="store_true", help="route is in or near a mine-danger area")
    p.add_argument("--closed", action="store_true",
                   help="closed or restricted: INPA list, HFC, closed military area, or a firing zone without confirmed coordination")
    p.add_argument("--upstream-rain", action="store_true",
                   help="rain over the catchment on the hike day or the day before, observed or forecast")
    p.add_argument("--wadi", action="store_true", help="route runs in a wadi bed or canyon")
    p.add_argument("--heatwave", action="store_true", help="IMS heat-wave warning (type 33) for the area")
    p.add_argument("--firing-unsure", action="store_true", help="unclear whether the route crosses a firing zone")
    p.add_argument("--weekend", action="store_true", help="hike is on a Friday, Shabbat or holiday")
    p.add_argument("--judea-samaria", action="store_true", help="route is in Judea and Samaria (outside Area A)")
    p.add_argument("--organized", action="store_true", help="school, youth movement or other Ministry of Education framework")
    p.add_argument("--checked", default="", help="checks completed, comma-separated: " + ",".join(CHECKS))
    a = p.parse_args(argv)
    try:
        card, code = build(a)
    except (ValueError, TypeError, KeyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(card)
    return code


if __name__ == "__main__":
    sys.exit(main())
