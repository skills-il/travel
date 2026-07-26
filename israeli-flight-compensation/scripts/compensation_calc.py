#!/usr/bin/env python3
"""Compute flight compensation under Israel's Aviation Services Law, 2012 (Tibi Law).

All amounts are the in-force figures as of 2026. They are CPI-updated every
January 1 and rounded to the nearest 10 NIS, so confirm the current-year amount
before relying on the output. This is Israel's own law, NOT EU261. Do not use
EU261 amounts for an Israel-nexus flight.

Usage:
  python compensation_calc.py --distance-km 3000 --delay-hours 9
  python compensation_calc.py --distance-km 1500 --event cancellation --notice-days 5
  python compensation_calc.py --distance-km 6000 --delay-hours 9 \
      --alternative-accepted --alternative-arrival-delay-hours 3
  python compensation_calc.py --example
"""

import argparse
import json
import sys

# 2026 in-force monetary compensation by distance band (NIS).
BANDS = [
    {"max_km": 2000, "amount": 1530, "alt_window_hours": 2},
    {"max_km": 4500, "amount": 2450, "alt_window_hours": 3},
    {"max_km": None, "amount": 3670, "alt_window_hours": 4},  # over 4,500 km
]

# 2026 in-force DOMESTIC monetary compensation (NIS). Domestic flights are NOT
# paid on the First Schedule bands above: section 18 of the law defers them to
# separate regulations (טיסות פנים-ארציות, 2013) with their own amounts.
DOMESTIC_ROUTES = {
    "eilat": {"amount": 300,
              "desc": "Tel Aviv (Sde Dov), Ben Gurion or Haifa to/from Eilat"},
    "ein_yahav_rosh_pina": {"amount": 180,
                            "desc": "Tel Aviv (Sde Dov) to/from Ein Yahav or Rosh Pina (Mahanayim)"},
    "other": {"amount": 240, "desc": "any other domestic route"},
}

# Section 11 exemplary damages: up to 10,000 NIS as written, indexed to 12,240
# NIS for 2026. Awarded at the court's discretion for a KNOWING breach of
# sections 5, 6, 7, 8, 9(b) or 10. Separate from, and on top of, the band amount.
EXEMPLARY_DAMAGES_MAX_2026 = 12240

INTL_DELAY_CANCELLATION_HOURS = 8
DOMESTIC_DELAY_CANCELLATION_HOURS = 3
CANCELLATION_NOTICE_DAYS = 14
LIMITATION_YEARS = 4

EVENTS = ("cancellation", "delay", "denied_boarding", "early_departure", "downgrade")


def band_for_distance(distance_km):
    for b in BANDS:
        if b["max_km"] is None or distance_km <= b["max_km"]:
            return b
    return BANDS[-1]


def assess(distance_km, event, delay_hours, notice_days, domestic,
           alternative_accepted, alternative_arrival_delay_hours, exemption,
           domestic_route="other", passengers=1, ticket_type="unknown"):
    notes = []
    if ticket_type in ("free", "non_public"):
        notes.append(
            "Section 2(b)(2): a ticket received free of charge, or bought at a special fare "
            "not available to the public, carries NO entitlement to any benefit. The "
            "exception is a ticket issued under a frequent-flyer or benefits programme, "
            "which IS covered. No amount is computed."
        )
        return {
            "eligible_for_money": False,
            "amount_nis": 0,
            "passengers": passengers,
            "total_for_all_passengers_nis": 0,
            "exemplary_damages_max_nis_per_passenger": 0,
            "band_distance_km": None,
            "notes": notes,
            "limitation_years": LIMITATION_YEARS,
        }
    if ticket_type == "unknown":
        notes.append(
            "Ticket type not stated. Confirm it was not free and not a non-public special "
            "fare before relying on this amount (section 2(b)(2)); an award ticket bought "
            "with points IS covered.")
    if domestic:
        route = DOMESTIC_ROUTES.get(domestic_route, DOMESTIC_ROUTES["other"])
        band = {"amount": route["amount"], "alt_window_hours": None}
        base = route["amount"]
        notes.append(
            "Domestic flight: paid under the domestic regulations, NOT the "
            "international distance bands. Route category: %s = %d NIS (2026)."
            % (route["desc"], route["amount"])
        )
    else:
        band = band_for_distance(distance_km)
        base = band["amount"]

    # Decide whether a monetary trigger applies.
    eligible = False
    if event == "delay":
        threshold = DOMESTIC_DELAY_CANCELLATION_HOURS if domestic else INTL_DELAY_CANCELLATION_HOURS
        if delay_hours is not None and delay_hours >= threshold:
            eligible = True
            notes.append(
                f"Delay of {delay_hours}h meets the {threshold}h "
                f"{'domestic' if domestic else 'international'} threshold; treated as a cancellation."
            )
        else:
            notes.append(
                f"Delay under the {threshold}h threshold: assistance only, no monetary compensation."
            )
    elif event == "cancellation":
        if notice_days is not None and notice_days < CANCELLATION_NOTICE_DAYS:
            eligible = True
            notes.append(f"Cancellation with {notice_days} days notice (under 14): monetary compensation applies if no qualifying alternative was offered.")
        else:
            notes.append("Cancellation with 14+ days notice: generally no monetary compensation.")
    elif event == "denied_boarding":
        eligible = True
        notes.append("Involuntary denied boarding (no voluntary give-up of seat): monetary compensation applies.")
    elif event == "early_departure":
        early_threshold = (DOMESTIC_DELAY_CANCELLATION_HOURS if domestic
                           else INTL_DELAY_CANCELLATION_HOURS)
        if delay_hours is not None and delay_hours > early_threshold:
            eligible = True
            notes.append(
                "Early departure of more than %gh with short notice: monetary compensation applies."
                % early_threshold)
        else:
            notes.append(
                "Early departure of %gh or less: refund/alternative only, no monetary "
                "compensation. Note an early departure of more than 5 and up to 8 hours "
                "still entitles the passenger to a refund or an alternative flight."
                % early_threshold)
    elif event == "downgrade":
        notes.append("Downgrade: compensation is a percentage of the ticket price per the law's Second Schedule. See references/compensation-table.md for the exact percentages by class transition.")
        notes.append(
            "Downgrade is a percentage of the ticket price the passenger PAID, so it cannot "
            "be computed from distance alone. On a package tour or charter with no separable "
            "ticket price, use the Third Schedule deemed prices in "
            "references/compensation-table.md.")
        notes.append(
            "Section 7 is one of the sections listed in section 11, so exemplary damages of "
            "up to %d NIS per passenger can be claimed on a downgrade too."
            % EXEMPLARY_DAMAGES_MAX_2026)
        return {
            "eligible_for_money": False,
            "amount_nis": None,
            "passengers": passengers,
            "total_for_all_passengers_nis": None,
            "exemplary_damages_max_nis_per_passenger": EXEMPLARY_DAMAGES_MAX_2026,
            "band_distance_km": distance_km,
            "notes": notes,
            "limitation_years": LIMITATION_YEARS,
        }

    amount = base if eligible else 0

    # 50% reduction for an accepted alternative arriving within the window.
    if eligible and alternative_accepted and band.get("alt_window_hours") is None:
        notes.append(
            "You passed --alternative-accepted on a DOMESTIC flight. The 2/3/4-hour reduction "
            "windows are set by distance band and have no domestic equivalent in the "
            "regulations, so no reduction was applied here. Confirm against the domestic "
            "regulations before telling the passenger the full amount is safe.")
    if eligible and alternative_accepted and band.get("alt_window_hours") is not None:
        window = band["alt_window_hours"]
        if alternative_arrival_delay_hours is not None and alternative_arrival_delay_hours <= window:
            amount = round(base / 2)
            notes.append(
                f"Accepted alternative arrived within {window}h of original: airline may pay half ({amount} NIS)."
            )
        else:
            notes.append(
                f"Accepted alternative arrived beyond the {window}h window: full amount stands."
            )

    if eligible and exemption:
        notes.append(
            "Exemption ASSERTED by the airline (%s). This is NOT applied automatically: "
            "section 6(e) puts the burden of proof on the carrier, and there are exactly "
            "three grounds, (1) extraordinary circumstances outside its control that it "
            "could not have prevented, (2) a protected strike or lockout, (3) avoiding "
            "desecration of Shabbat or a holiday. Israeli case law reads ground (1) "
            "narrowly, so a routine technical fault is usually not an exemption. Note "
            "ground (3) does not defeat an early-departure claim under section 8(b)(1), "
            "which cross-references only grounds (1) and (2). Treat the amount below as "
            "the claim to pursue unless the carrier actually proves its ground."
            % exemption
        )
        notes.append(
            "If the exemption is ultimately proven, the monetary compensation falls away "
            "but assistance, the refund, and the alternative-flight choice are still owed."
        )

    notes.append(
        "Separately, section 11 lets the court award exemplary damages of up to %d NIS "
        "(2026 indexed) per passenger, with no proof of harm, for a KNOWING breach. "
        "Claim it explicitly in the demand letter and the statement of claim; it is often "
        "larger than the band amount itself." % EXEMPLARY_DAMAGES_MAX_2026
    )

    return {
        "eligible_for_money": eligible and amount > 0,
        "amount_nis": amount,
        "passengers": passengers,
        "total_for_all_passengers_nis": amount * passengers,
        "exemplary_damages_max_nis_per_passenger": EXEMPLARY_DAMAGES_MAX_2026,
        "band_distance_km": None if domestic else distance_km,
        "notes": notes,
        "limitation_years": LIMITATION_YEARS,
    }


def main():
    p = argparse.ArgumentParser(description="Israel Aviation Services Law compensation calculator (2026 figures)")
    p.add_argument("--distance-km", type=float)
    p.add_argument("--event", choices=EVENTS, default="delay")
    p.add_argument("--delay-hours", type=float, default=None,
                   help="Hours of delay at departure (for delay/early_departure events)")
    p.add_argument("--notice-days", type=int, default=None,
                   help="Days of advance notice (for cancellation)")
    p.add_argument("--domestic", action="store_true",
                   help="Domestic Israeli flight (3h threshold AND the separate domestic amounts)")
    p.add_argument("--domestic-route", choices=tuple(DOMESTIC_ROUTES),
                   default="other",
                   help="Which domestic route category (sets the amount): "
                        "eilat=300, ein_yahav_rosh_pina=180, other=240 NIS (2026)")
    p.add_argument("--passengers", type=int, default=1,
                   help="Number of ticketed passengers; each has a separate claim")
    p.add_argument("--alternative-accepted", action="store_true")
    p.add_argument("--alternative-arrival-delay-hours", type=float, default=None)
    p.add_argument("--exemption", default=None,
                   help="Exemption reason if the airline claims one (e.g. extraordinary, iron_swords)")
    p.add_argument("--ticket-type",
                   choices=("paid", "award", "free", "non_public", "unknown"),
                   default="unknown",
                   help="How the ticket was obtained. free/non_public are excluded from all "
                        "benefits under s.2(b)(2); award (frequent-flyer) IS covered")
    p.add_argument("--example", action="store_true")
    args = p.parse_args()

    if args.example:
        demo = assess(3000, "delay", 9, None, False, False, None, None)
        print(json.dumps(demo, ensure_ascii=False, indent=2))
        return 0

    if args.distance_km is None and not args.domestic:
        p.error("--distance-km is required for an international flight (or use --example)")
    if args.passengers < 1:
        p.error("--passengers must be at least 1")
    if args.event in ("delay", "early_departure") and args.delay_hours is None:
        p.error("--delay-hours is required for a %s event; without it the result would "
                "wrongly read as 'no compensation owed'" % args.event)
    if args.event == "cancellation" and args.notice_days is None:
        p.error("--notice-days is required for a cancellation event")

    result = assess(
        args.distance_km, args.event, args.delay_hours, args.notice_days,
        args.domestic, args.alternative_accepted, args.alternative_arrival_delay_hours,
        args.exemption, args.domestic_route, args.passengers, args.ticket_type,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
