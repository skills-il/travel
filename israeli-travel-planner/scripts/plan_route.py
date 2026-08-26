#!/usr/bin/env python3
"""Plan routes between Israeli cities with transport options.

Calculates distances and suggests transportation modes between
major Israeli cities and tourist destinations.

Usage:
    python plan_route.py --from "tel-aviv" --to "jerusalem"
    python plan_route.py --from "haifa" --to "eilat"
    python plan_route.py --from "תל אביב" --to "ירושלים"
    python plan_route.py --list
    python plan_route.py --help

Hebrew city names are accepted as well as the English slugs.
Times are rough averages from a flat speed model, not timetables. Always
confirm against Moovit or the operator before giving them to a traveler.

Requirements:
    Python 3.9+ (no external dependencies)
"""

import argparse
import sys


# Distance matrix (km) between major cities
# Derech Shava distance bands, BUS column (bus, light rail, Metronit,
# Rakavlit, Carmelit). A journey including Israel Railways is priced on the
# separate, higher combined-rail column, which this table deliberately omits.
# Source: https://bus.gov.il/FaresDistance
FARE_BANDS = [
    (15, "0-15 km (yellow)", 8.0, 17.5),
    (40, "15-40 km (green)", 14.5, 29.0),
    (75, "40-75 km (turquoise)", 19.0, 37.5),
    (120, "75-120 km (blue)", 19.0, 37.5),
    (225, "120-225 km (purple)", 30.5, 60.5),
    (float("inf"), "over 225 km (grey)", 74.0, 79.5),
]


def fare_band(distance_km):
    """Return (label, single_fare, daily_cap) for a road distance in km.

    Road distance approximates the fare distance; the operator's own figure
    governs, so this is guidance, not a quote.
    """
    for limit, label, single, cap in FARE_BANDS:
        if distance_km <= limit:
            return label, single, cap
    return FARE_BANDS[-1][1:]


DISTANCES = {
    ("tel-aviv", "jerusalem"): 60,
    ("tel-aviv", "haifa"): 95,
    ("tel-aviv", "beer-sheva"): 115,
    ("tel-aviv", "eilat"): 350,
    ("tel-aviv", "tiberias"): 130,
    ("tel-aviv", "netanya"): 30,
    ("tel-aviv", "ashdod"): 35,
    ("jerusalem", "haifa"): 155,
    ("jerusalem", "beer-sheva"): 80,
    ("jerusalem", "eilat"): 310,
    ("jerusalem", "dead-sea"): 40,
    ("jerusalem", "tiberias"): 165,
    ("haifa", "tiberias"): 65,
    ("haifa", "nazareth"): 35,
    ("haifa", "akko"): 25,
    ("haifa", "nahariya"): 35,
    ("beer-sheva", "eilat"): 240,
    ("beer-sheva", "dead-sea"): 100,
    ("haifa", "eilat"): 445,
    ("haifa", "jerusalem"): 155,
    ("haifa", "beer-sheva"): 200,
    ("haifa", "netanya"): 65,
    ("haifa", "ashdod"): 130,
    ("akko", "nahariya"): 12,
    ("akko", "tiberias"): 55,
    ("akko", "nazareth"): 45,
    ("nahariya", "tiberias"): 65,
    ("nazareth", "tiberias"): 30,
    ("nazareth", "tel-aviv"): 105,
    ("netanya", "haifa"): 65,
    ("netanya", "jerusalem"): 90,
    ("ashdod", "jerusalem"): 65,
    ("ashdod", "beer-sheva"): 65,
    ("eilat", "dead-sea"): 200,
    ("tiberias", "beer-sheva"): 240,
    ("dead-sea", "tel-aviv"): 110,
    ("ben-gurion", "tel-aviv"): 20,
    ("ben-gurion", "jerusalem"): 45,
    ("ben-gurion", "haifa"): 110,
    ("ben-gurion", "beer-sheva"): 95,
    ("ben-gurion", "netanya"): 45,
}

# Hebrew aliases so a Hebrew-speaking user can pass native place names.
CITY_ALIASES = {
    "תל אביב": "tel-aviv", "תל-אביב": "tel-aviv",
    "ירושלים": "jerusalem", "חיפה": "haifa",
    "באר שבע": "beer-sheva", "באר-שבע": "beer-sheva",
    "אילת": "eilat", "טבריה": "tiberias",
    "נתניה": "netanya", "אשדוד": "ashdod",
    "ים המלח": "dead-sea", "נצרת": "nazareth",
    "עכו": "akko", "נהריה": "nahariya",
    "נתב\"ג": "ben-gurion", "נמל התעופה בן גוריון": "ben-gurion",
    "בן גוריון": "ben-gurion", "שדה התעופה": "ben-gurion",
    "תל אביב יפו": "tel-aviv", "תל אביב-יפו": "tel-aviv",
}


def resolve_city(name):
    """Map a Hebrew name or an English slug to the canonical slug."""
    key = name.strip()
    if key in CITY_NAMES_HE:
        return key
    return CITY_ALIASES.get(key)

# Transport options with estimated times
TRANSPORT = {
    "train": {"name": "רכבת ישראל", "speed_kmh": 90,
              "note": "no service Shabbat/chag; resumes Sat night"},
    "bus": {"name": "אוטובוס", "speed_kmh": 60,
            "note": "state service stops Shabbat/chag; some cities run weekend service, check per city"},
    "car": {"name": "רכב פרטי", "speed_kmh": 80,
            "note": "Hwy 6 + Carmel Tunnels are barrier-free tolls; on a rental they are rebilled with a fee"},
    "sherut": {"name": "מונית שירות", "speed_kmh": 70,
               "note": "corridor-specific, NOT nationwide; confirm this route exists before offering it"},
}

# Train routes (city pairs served by Israel Railways)
TRAIN_ROUTES = {
    ("tel-aviv", "jerusalem"), ("tel-aviv", "haifa"), ("tel-aviv", "beer-sheva"),
    ("tel-aviv", "netanya"), ("tel-aviv", "ashdod"), ("haifa", "nahariya"),
    ("haifa", "akko"), ("akko", "nahariya"),
    ("netanya", "haifa"), ("tel-aviv", "akko"), ("tel-aviv", "nahariya"),
    ("ben-gurion", "tel-aviv"), ("ben-gurion", "jerusalem"),
    ("ben-gurion", "haifa"), ("ben-gurion", "beer-sheva"),
}

CITY_NAMES_HE = {
    "tel-aviv": "תל אביב",
    "jerusalem": "ירושלים",
    "haifa": "חיפה",
    "beer-sheva": "באר שבע",
    "eilat": "אילת",
    "tiberias": "טבריה",
    "netanya": "נתניה",
    "ashdod": "אשדוד",
    "dead-sea": "ים המלח",
    "nazareth": "נצרת",
    "akko": "עכו",
    "nahariya": "נהריה",
    "ben-gurion": "נתב\"ג",
}


def get_distance(city_a, city_b):
    """Get distance between two cities."""
    key = (city_a, city_b)
    if key in DISTANCES:
        return DISTANCES[key]
    key = (city_b, city_a)
    if key in DISTANCES:
        return DISTANCES[key]
    return None


def has_train(city_a, city_b):
    """Check if train service exists between cities."""
    return (city_a, city_b) in TRAIN_ROUTES or (city_b, city_a) in TRAIN_ROUTES


def plan_route(origin, destination):
    """Plan a route between two cities."""
    distance = get_distance(origin, destination)
    if distance is None:
        print(
            f"No distance data for {origin} -> {destination}. This script only "
            f"covers a fixed matrix of city pairs; use Moovit or the operator "
            f"for anything not listed.",
            file=sys.stderr,
        )
        return 1

    origin_he = CITY_NAMES_HE.get(origin, origin)
    dest_he = CITY_NAMES_HE.get(destination, destination)

    print(f"\nRoute: {origin_he} -> {dest_he}")
    print(f"Distance: {distance} km\n")
    print("Transport options:")
    print("-" * 60)

    for mode, info in TRANSPORT.items():
        if mode == "train" and not has_train(origin, destination):
            print(f"  {info['name']}: No direct train service")
            continue

        hours = distance / info["speed_kmh"]
        mins = int(hours * 60)
        print(f"  {info['name']}: ~{mins} min ({info['note']})")

    label, single, cap = fare_band(distance)
    print(f"\nDerech Shava band: {label}")
    print(f"  Bus single ride: {single:g} NIS   Bus daily cap: {cap:g} NIS")
    print("  These are the BUS column. A journey including Israel Railways is")
    print("  priced on the higher combined-rail column, so do NOT quote these")
    print("  figures for a train leg. Live table: https://bus.gov.il/FaresDistance")
    print("\nTimes are estimates from a flat speed model over ROAD distance, not")
    print("timetables, so rail times in particular are approximate. Confirm on")
    print("Moovit or with the operator before giving them to a traveler.")
    print()
    return 0


def main():
    cities = list(CITY_NAMES_HE.keys())
    parser = argparse.ArgumentParser(description="Plan routes between Israeli cities")
    parser.add_argument("--from", dest="origin", help="City slug or Hebrew name")
    parser.add_argument("--to", dest="destination", help="City slug or Hebrew name")
    parser.add_argument("--list", action="store_true", help="List supported cities and exit")
    args = parser.parse_args()

    if args.list:
        for slug in cities:
            print(f"{slug:12s} {CITY_NAMES_HE[slug]}")
        return 0

    if not args.origin or not args.destination:
        parser.error("--from and --to are required (or use --list)")

    origin = resolve_city(args.origin)
    destination = resolve_city(args.destination)
    for raw, resolved in ((args.origin, origin), (args.destination, destination)):
        if resolved is None:
            print(f"Unknown city: {raw}", file=sys.stderr)
            print(f"Supported: {', '.join(cities)}", file=sys.stderr)
            print("Hebrew names are also accepted; run --list to see them.", file=sys.stderr)
            return 2

    return plan_route(origin, destination)


if __name__ == "__main__":
    sys.exit(main())
