---
name: israeli-hiking-day-planner
description: "Not a safety clearance, official closures and warnings always override it. Plan a day hike in Israel and get a go, caution or no-go call plus a printable route card. Checks the IMS hourly heat-stress forecast and warnings, flash-flood risk from rain upstream, INPA closed trails and site hours, Home Front Command restrictions, mine areas and IDF firing zones, then works out the latest safe start, a finish before dark and water per person from official INPA and Ministry of Education figures. Use when someone asks if a trail is OK this weekend, plans a hike in the Negev, Judean Desert, Dead Sea, Galilee or Golan, or asks how much water to bring, when to start, or what to do in an emergency on the trail. Do NOT use for general domestic trip planning, accommodation or transport (use israeli-travel-planner), trips abroad, or multi-day treks and camping."
license: MIT
---

# Israeli Hiking Day Planner

## Legal notice

This skill is a planning aid built from published sources (IMS, INPA, the Ministry of Education, Home Front Command and the IDF). It is not a safety clearance, not a licensed guide, and not the Ministry of Education's trip approval for a school or youth group. It never declares a trail "safe": the strongest result is "no official warning found at the time of checking". Conditions change within hours. INPA closures, IMS warnings, Home Front Command instructions and IDF closures always override the route card, and the decision to go, and responsibility for the group, stay with the hikers.

## Problem

Two of the deadliest hiking hazards in Israel are invisible from the trailhead: a heat-stress afternoon in the Judean Desert, and a flash flood in a dry canyon where the sun is shining because the rain fell upstream (the May 2007 Nahal Kumran disaster killed four hikers that way). The facts that decide a hike live in five places (IMS, INPA, Home Front Command, the IDF, and the site's own hours) and change daily. This skill checks all of them for the user's date and route and turns the result into one decision and a route card.

## Instructions

### Step 1: Pin down the hike

Collect, asking only for what is missing:

- Trail or area, and date. Friday and holiday-eve hours are shorter at INPA sites, and firing-zone coordination closes when Shabbat or a holiday begins (step 3.1).
- **Private group or an organized framework?** A school, youth movement or other Ministry of Education framework works under the Ministry's standing orders: the trip needs the Ministry's approval and coordination through its trips situation room (02-6222211), firing-zone requests go in at least 21 days ahead, and on flood-prone routes the leader must contact the situation room the evening before and again on the morning of the trip before entering the stream. This route card does not replace any of that; point the leader to it and keep planning as a supporting tool.
- Group: number of people and the ages of any children.
- Car shuttle or a loop, and whether the user has a planned start time.
- Region for water: INPA splits its water guidance into north (3 L per person) and south (5 L per person). Treat the Negev, Arava, Eilat mountains, Dead Sea and Judean Desert as south.

### Step 2: Get the route and its real duration

- `find_trails` (israel-hiking MCP) is a NAME search over an area string, not a radius search. Search by trail or stream name ("Nahal Arugot"), not by "trails near me".
- `plan_route` returns distance, an elevation profile (ascent, descent, min, max) and a road-type breakdown. It returns NO duration, NO difficulty and NO closure status. Never present a difficulty grade as if the MCP supplied it.
- `search_pois` finds parking, water sources and viewpoints near the route.
- **Duration:** use the walking time INPA publishes for the route when there is one (the Hidden Waterfall in Nahal Arugot is about 3-4 hours round trip; the Lower Pools about 20 minutes each way), or ask INPA's information line *3639. The distance-and-ascent rule in step 4 is a minimum, not a plan, and it is badly short for boulder-hopping, wading, ladders and children.
- INPA also describes who a route suits. The Hidden Waterfall route is "challenging, exposed to the sun, for experienced hikers"; the Lower Pools route is "short, suits the whole family". Read that line before picking a route for children.
- OpenStreetMap routing can follow unmarked or closed paths. INPA allows walking and driving on marked trails only, so check that the route stays on a marked trail.

### Step 3: Run the checks, in this order

Stop at the first hard no-go and say which check failed. Record which checks you completed: a check you could not complete (a page would not load, the user did not paste it) is never a pass.

1. **Closed or restricted ground.**
   - INPA closed-trails page and newsflashes (מבזקים): INPA tells hikers to check the newsflashes before every hike. No MCP covers INPA status, so open the page or send the user to it.
   - Mines: INPA bans leaving marked trails in listed northern reserves (Snir-Hatzbani, Yehudiya, Meshushim, Hermon-Banias, Tel Dan and more). Anywhere in the country, do not enter areas suspected of mines or marked with yellow signs or red triangles, and never cross a minefield fence.
   - Home Front Command (פיקוד העורף): check the defense policy for the hike's zone on the day. Under a restriction, a "gathering" means more than 10 people, which can catch a group hike.
   - IDF firing zones (שטחי אש) and closed military areas: entry to a closed area needs a written permit from a military commander. In its notice for the Shavuot weekend of May 2026 (as reported by Srugim), Southern Command said every arrival in a military area or an open firing zone needs prior coordination and approval through its coordination office (מתא"ם), that some zones stay fully closed while others open by the army's official schedules and maps, and that coordination could be done only until the holiday began. Treat that as the rule unless the IDF's current notice says otherwise: a Friday, Shabbat or holiday route through a firing zone without coordination already confirmed is a NO-GO, not a "coordinate first". No current official phone number was found on an IDF page, so do not print one; tell the user to use the coordination office details the IDF publishes with its weekend and holiday openings. If you cannot tell whether the route crosses a firing zone, say so: on a Friday, Shabbat or holiday that is a NO-GO, on a weekday a CAUTION.
   - This skill does not plan routes in Area A of Judea and Samaria. Elsewhere in Judea and Samaria it does not assess security conditions: check the Home Front Command zone and current notices, and mark the card CAUTION.
2. **IMS warnings.** Call `get_ims_alerts`. Relevant warning types: heat stress (8), floods (5), flooding (7), thunderstorms (11), fire danger (10), heat wave (33). Severities run yellow, orange and red.
   - A flood, flooding or thunderstorm warning for a wadi, a canyon or an exposed summit: NO-GO.
   - Any orange or red warning covering the hike area: NO-GO (this skill's rule).
   - A heat-wave warning (type 33) for the area, at any severity: NO-GO. INPA says hiking is forbidden on sharav days (this skill reads a heat-wave warning as a sharav day).
   - Any other yellow warning: CAUTION, and read its hours.
   - Fire danger: CAUTION, no fire of any kind, and check closures.
3. **Hourly heat stress.** Call `get_forecast_data` for the IMS location nearest the trailhead. IMS has locations at reserves too (80 Ein Gedi, 267 Masada, 261 Qumran, 255 Ein Prat, 211 Nahal Amud, 704 Ramon), so prefer those to the nearest city. Classify each hike hour from the NUMERIC `heat_stress` value using the scale below. Do NOT use `heat_stress_level`: it does not match the published scale (28.4, which is heavy, comes back as 3).
4. **Flash floods.** In the rainy season, check the IMS forecast for the high ground the stream drains from, not just the trailhead, and look for rain over the whole catchment that day. On 04/05/25 more than 30 mm fell in 10 minutes over the David and Arugot basins, and Nahal Arugot passed 200 m3/s, while no rain fell on more than 90% of its catchment. If rain falls or is forecast over the catchment on the hike day or the day before, treat the wadi as flood risk too: a flood can arrive long after the rain stops (this skill's conservative rule). A wadi or canyon route whose flood check was not completed is a NO-GO. Pass the outcome to the script: `--checked ...,flood` once you have looked, `--upstream-rain` if the check found rain over the catchment on the hike day or the day before (observed or forecast), `--flood-warning` for an IMS flood, flooding or thunderstorm warning, and `--wadi` for a stream-bed or canyon route. Never cross a flowing wadi on foot or by car, and avoid narrow canyons on any day with rain in the forecast. If water rises or turns muddy while you are in a stream bed, get out onto high ground at once, and never park a car in a wadi bed.
5. **Daylight and site hours.** Get sunrise and sunset for the trailhead coordinates (hebcal MCP; pass them as `--sunrise` and `--sunset`; the IMS forecast API returns no sunrise or sunset, and Hebcal is not a government source). Read the site's opening, last-entry and exit times from its INPA page, including the Friday and holiday-eve hours (Nahal Arugot in winter: Sun-Thu and Saturday 08:00-16:00, Fridays and holiday eves 08:00-15:00). INPA's hours at Nahal Arugot extend by one hour in summer time, so check whether the hike date falls in summer time.

### Step 4: Compute the plan

Run `scripts/hike_plan.py` (no network access) with the numbers from steps 2 and 3, or apply the same rules by hand:

- **Walking time:** the longer of the route's published or confirmed duration and the minimum rule of 5 km per hour plus one minute per 10 m of ascent (from UK licensing regulations, the metric form of Naismith's rule, not an Israeli source). When INPA gives a range (3-4 h), plan with the upper end. Without a published or confirmed duration the result can be no better than CAUTION, and the latest safe start it prints is not reliable.
- **Finish by:** the earlier of one hour before sunset (the Ministry of Education rule for school trips; INPA says finish before dark) and the earliest exit time that applies to the route (at Arugot, leave the Hidden Waterfall by 14:30 in winter, not just the reserve by 16:00).
- **Latest safe start:** finish-by minus walking time, and no later than the site's last entry. If the site opens after the latest safe start, the route does not fit the day.
- **Heat window:** every hourly reading from the start hour through the first reading at or after the finish must stay below heavy heat stress. With moderate hours in the window, plan to finish before them and avoid exertion 10:00 to 16:00. With children under 10 in the south, a moderate hour inside the window is a NO-GO (this skill's conservative rule). If heavy heat comes later the same day, keep a margin: INPA advises giving up the hike on sharav days.
- **Water per person:** the highest of the INPA regional figure, the INPA figure for that site if one is published, and the Ministry of Education daily minimum (1.5 L regular day, 3 L hot day, 4.5 L heat load). The circular does not tie its day types to IMS bands; this skill reads no heat stress as a regular day, light or mild as a hot day, and moderate or above as heat load. For children, also show the Ministry heat-card drinking rate (ages 6-10 half a liter per walking hour, 11-18 three quarters of a liter) as a schedule, never as a smaller total.

### Step 5: Decide, using exactly these words

| Decision | When |
|---|---|
| NO-GO | Any check in step 3.1 fails, including an unclear firing zone on a Friday, Shabbat or holiday; a flood, flooding or thunderstorm warning on a wadi, canyon or exposed-summit route; rain over the catchment on the hike day or the day before (observed or forecast) on a wadi or canyon route, or a wadi route without a completed flood check; an orange or red IMS warning, or a heat-wave warning, for the area; heavy or extreme heat stress inside the hike window; a moderate hour inside the window with children under 10 in the south; the planned start is after the latest safe start, or the site opens too late for the route |
| CAUTION | Moderate heat stress in the window, heavy heat later the same day, missing hourly data, a yellow IMS warning or a fire-danger warning, a mine-danger area (stay on the marked trail), no published or confirmed duration, unsure on a weekday whether the route crosses a firing zone, a route in Judea and Samaria, a planned start before the site opens or before sunrise, checks done before the hike day (re-check that morning), or any check not completed |
| NO OFFICIAL WARNING FOUND | Nothing above applies. Say when you checked, and that conditions change |

For a NO-GO, offer an alternative: an earlier start, a shorter variant (at Arugot, the Lower Pools instead of the Hidden Waterfall), a shaded or northern trail, or another day. For a school or youth group, add that the card is not the Ministry's trip approval.

### Step 6: Hand over the route card

Output the route card from the script (or the same layout): decision, timing table, hourly heat bands, water, equipment and the emergency plan. Put the hike date and the time of the checks on the card (`--date`, `--checked-at`).

## IMS Heat-Stress Scale

IMS computes the index as (dry temperature + wet-bulb temperature) / 2.

| Index (units) | Band | Hebrew |
|---|---|---|
| below 22.0 | none | אין עומס חום |
| 22.0 to 23.9 | light | קל |
| 24.0 to 25.9 | mild | מתון |
| 26.0 to 27.9 | moderate | בינוני |
| 28.0 to 29.9 | heavy | כבד |
| 30.0 and above | extreme | קיצוני |

What the official bodies do with it:

- INPA: give up the hike on sharav days and on days with flood danger.
- Ministry of Education (schools): heavy heat stress forecast the evening before at the destination means no field trips; heavy heat all day means no activity.
- Masada (INPA, by the IMS forecast): moderate heat, last ascent of the Snake Path 10:00 and last descent 11:00; heavy heat, the Snake Path closes 08:00 for ascent and 09:00 for descent. In summer extreme heat the Snake Path closes 07:00 / 08:00, the Ramp Path 11:00 / 12:00, and the Runner's Path and Ma'ale Elazar 07:00.
- Ein Gedi: in 2025 INPA closed all ascents in the reserve "until September" for heat stress. Heat closures elsewhere are announced per site and per season, not from a standing table.

## Water

| Source | Figure | Applies to |
|---|---|---|
| INPA | 3 L per person north, 5 L per person south | All hikers |
| INPA, Nahal Arugot | 3 L to the Hidden Waterfall, at least 4 L to the upper pools | That site |
| Ministry of Education circular (2016) | Minimum on foot per day: 1.5 L regular day, 3 L hot day, 4.5 L heat load | School trips |
| Ministry of Education heat card | Half a liter per walking hour (ages 6-10), three quarters (11-18); about a third of a liter every half hour | School trips |

Vigorous activity on a hot day can lose 1 to 1.5 liters of fluid per hour, which is why the southern figure is a floor and not a target. Most dehydration and heat-stroke events in Ministry records happened on the first day in the field, before acclimatization. Never drink from springs, pools or stream beds the Ministry of Health has not approved. In October 2026 INPA reported several northern streams above the Ministry of Health recommendation of 400 fecal coliforms per 100 ml; check its water-quality notice before a wet hike in the north.

## Equipment

INPA's list: enough water and food, suitable clothing, walking shoes, sunscreen, a head cover, and a mobile phone with a charged battery. At Nahal Arugot INPA requires a hat and closed walking shoes, not flip-flops. Because walking in the dark is forbidden and a delayed group can still be caught by it, this skill also adds a flashlight or headlamp to every card.

## Site Rules Worth Knowing

- **Ein Gedi, Nahal Arugot:** advance registration only. Hidden Waterfall: opens 08:00, last entry 13:00, leave the waterfall by 14:30 and the reserve by 16:00. Lower Pools: leave the pools by 15:30. Upper pools: 4-6 h round trip, at least 4 L each, ascend from the waterfall by 12:30 and leave the upper pools by 13:30. These are winter hours; in summer time INPA's hours here extend by one hour. Fridays and holiday eves close at 15:00 in winter. No fire of any kind, including gas stoves and cigarettes.
- **Masada:** the Snake Path opens for ascent about one hour before sunrise and closes for ascent two hours before the site closes.
- **All reserves and national parks:** lighting a fire inside them is strictly forbidden, and jumping into water is forbidden.

## Emergency Plan (put this on every card)

- Medical emergency (heat illness, a fall, a bite): MDA 101. Distress, a lost hiker or a rescue: police 100. INPA also lists ZAKA 1220.
- Tell the dispatcher the exact location, what happened and what help is needed. In deep canyons the phone may have no signal; agree in advance where you would climb to get one.
- Heat illness: the Ministry of Education treats any symptom as a suspected start of heat stroke. Warning signs include severe headache, weakness, nausea, vomiting, little urine, dizziness, confusion and a flushed face. Stop, move the person into shade off the hot ground, and call 101.
- Unexploded ordnance or a suspicious object: do not touch or approach it, move away at once, and call 100. Children pick up fragments; brief them before the hike.
- Caught by dark: stop, stay on the trail and call for help. Someone separated from the group sits where they are and waits.
- Before leaving, put a written note on the car window or at the INPA site: names, phone, route, group size and schedule. Tell someone at home. There is no free official civilian "register your hike" service; SPNI's Moked Teva serves subscribers only. INPA's information line *3639 answers route questions (duration, age fit, water sources, weather).

## Without MCP Access (chat apps)

On Claude.ai, ChatGPT and other chat surfaces the MCPs are not available. Do the same checks by reading the official pages directly (web browsing if the surface has it, otherwise ask the user to open them and paste what they see): the IMS warnings page, the IMS forecast JSON for the location (`https://ims.gov.il/he/forecast_data/<location id>`), the INPA closed-trails page and the site page, and the Home Front Command policy page. Compute timing and water by hand with the rules in Step 4. Never fill a missing forecast with a guess; mark the card CAUTION and say which data is missing.

## Examples

### Example 1: Desert stream with kids

User says: "Is Nahal Arugot OK with our kids, 9 and 7? We want the waterfall."
Actions: read the INPA Ein Gedi page (registration, hours, who each route suits, duration) and the newsflashes, call `get_ims_alerts`, pull hourly heat for location 80, get sunset, run the script with the Hidden Waterfall's 3-4 h and its 14:30 exit.
Result (illustration: the IMS forecast for 23/10/2026 applied to INPA's winter weekday hours, last entry 13:00 and waterfall exit 14:30): with 08:00 23.0 light, 12:00 26.4 moderate, 13:00 27.2 moderate, 15:00 28.4 heavy, and a yellow IMS heat warning for the Dead Sea from 12:00, an 08:00 start at the upper end of INPA's 3-4 h reaches the 12:00 moderate hour: NO-GO for children under 10 under this skill's rule, and INPA itself calls the route one for experienced hikers. The card offers the Lower Pools (about 20 minutes each way, "suits the whole family") from 08:00 instead, with 5 L each: CAUTION for the yellow warning and the heavy heat later in the day. A 13:00 start to the waterfall walks into the 15:00 heavy hour: NO-GO for anyone.

### Example 2: Galilee loop in November

User says: "Plan a 10 km moderate loop in the Galilee for 4 adults in November."
Actions: `find_trails` by named streams in the area, `plan_route` for distance and ascent, ask *3639 or the trail's page for its walking time, check the INPA closed list and the mine-danger reserves, heat and rain for the nearest IMS location and the high ground upstream, sunset.
Result: the latest start counted back from an hour before an early November sunset using the confirmed duration, 3 L each (INPA north), and a reminder that early rains make stream crossings a flood question. With only the minimum walking-time rule, the card stays at CAUTION.

### Example 3: Negev in July, on a Saturday

User says: "We're going to the Negev on Saturday in July, what should we watch for?"
Actions: hourly heat for the nearest IMS location, IMS heat warnings, whether the route crosses a firing zone.
Result: most July hours in the desert reach heavy or extreme heat, so the plan is a dawn start that ends before the first heavy hour, with 5 L each as a floor. If the route crosses a firing zone and coordination was not confirmed before Shabbat, it is a NO-GO for this weekend; offer a route outside the zone.

## Bundled Resources

| File | Purpose |
|---|---|
| `scripts/hike_plan.py` | Offline calculator: heat bands per hour, walking time, latest start, water, equipment, Markdown route card. Flags: `--sunrise`, `--date`, `--checked-at`, `--wadi`, `--upstream-rain`, `--flood-warning`, `--heatwave`, `--warning`, `--fire-danger`, `--mine-area`, `--closed`, `--weekend` (set automatically from `--date` for Friday and Saturday; pass it for holidays), `--firing-unsure`, `--judea-samaria`, `--organized`, and `--checked inpa,hfc,firing,ims,flood`. A Friday, Shabbat or holiday hike without a completed firing-zone check is a NO-GO. Exit 0 no NO-GO found, 1 NO-GO, 2 bad input |
| `references/domain-checklist.md` | Coverage checklist with sources, current-status notes and known bad figures |

## Recommended MCP Servers

| MCP | Use it for | Link |
|---|---|---|
| israel-hiking | Trail search, route distance and elevation, water sources and parking | [Install](https://agentskills.co.il/en/mcp/israel-hiking) |
| ims-weather | Hourly heat stress, rain, IMS warnings | [Install](https://agentskills.co.il/en/mcp/ims-weather) |
| hebcal | Sunset for the trailhead coordinates | [Install](https://agentskills.co.il/en/mcp/hebcal) |
| israel-nature | Optional: what plants and wildlife were observed near the route | [Install](https://agentskills.co.il/en/mcp/israel-nature) |

## Gotchas

- Agents read `heat_stress_level` from the IMS API and report one band too low at exactly the thresholds INPA uses. Classify from the numeric `heat_stress` value.
- Agents treat a sunny forecast at the trailhead as flood-safe. Desert floods come from rain upstream; check the catchment.
- Agents plan with the 5 km/h rule and hide the hot or dark hours the group will actually walk in. Use INPA's published duration.
- Agents invent a trail difficulty or duration and attribute it to the hiking MCP. It returns neither.
- Agents tell a Friday user to "coordinate the firing zone first". In the May 2026 Southern Command notice (as reported by Srugim), coordination closed when the holiday began; without it the route is a NO-GO for the weekend. Agents also print old firing-zone phone numbers from blogs.
- Agents use the daily maximum heat value. The decision depends on the hours the group will actually be walking.
- Agents quote Sunday-Thursday site hours for a Friday, or summer hours in winter, putting the last entry an hour late.

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| IMS warnings | https://ims.gov.il/he/IMSwarnings | Active heat, flood and storm warnings |
| IMS heat-stress study and scale | https://ims.gov.il/sites/default/files/2025-01/%D7%9E%D7%92%D7%9E%D7%95%D7%AA_%D7%A2%D7%95%D7%9E%D7%A1_%D7%97%D7%95%D7%9D%20%D7%95%D7%9C%D7%97%D7%95%D7%AA_29122024.pdf | Table 2, the six heat-stress bands |
| INPA safe hiking | https://www.parks.org.il/new/beticut/ | Water per region, marked trails, leaving a note |
| INPA closed trails | https://www.parks.org.il/newsflash/maslulim-2/ | Closures by region, mine areas |
| INPA Ein Gedi, Nahal Arugot | https://www.parks.org.il/reserve-park/arugot/ | Registration, durations, hours, water |
| Ministry of Education trip orders (2016) | https://meyda.education.gov.il/files/Bitachon/teyulim2016.pdf | Heat, water and flood rules for school trips |
| Ministry of Education heat card | https://meyda.education.gov.il/files/noar/heat_load.pdf | Water per walking hour by age, heat-illness signs |
| Home Front Command policy | https://www.oref.org.il/heb/articles/info/iron-swords/1100 | Restrictions by zone |
| State Comptroller on IDF training areas (2021) | https://library.mevaker.gov.il/sites/DigitalLibrary/Documents/2021/71B-Bitachon/2021-71B-403-idf-training.pdf | Written permit for closed areas, coordination office |

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| parks.org.il returns 403 to a fetch | Bot protection on INPA's site (verified 2026-10-23); the page loads in a normal browser | Open it in a browser, or ask the user to open it and paste the alert text. Until then the INPA check is not done |
| `get_weather_analysis` fails | Its IMS endpoint returned a 301 redirect when checked on 2026-10-23 | Use `get_city_portal` (it carries the current analysis) and `get_forecast_data` |
| `find_trails` returns nothing | It searches names, not an area radius | Search by the stream or trail name, or use `search_pois` near coordinates |
| Heat values missing for some hike hours | The forecast did not cover those hours, or the wrong location id was used | Check the location id, and mark the card CAUTION until the hours are covered |
| The script exits 2 | A malformed time or heat value (expects `HH:MM` and `HH:value`) | Fix the argument; exit 2 is never a decision |
