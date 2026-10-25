# Flight Comparison Platforms for Israeli Travelers

## Pre-Filled Deep-Link Search URLs

Build a click-ready search for the traveler's exact route and dates, then open it to read the live fares (or hand it to the traveler). URL patterns taken from the platforms' own result pages:

| Platform | Round-trip template | Notes |
|----------|---------------------|-------|
| Google Flights | `https://www.google.com/travel/flights?q=Flights+from+TLV+to+{CITY}+on+{YYYY-MM-DD}+returning+{YYYY-MM-DD}&curr=ILS&gl=IL&hl=he` | Natural-language query; plain city name; `curr=ILS` forces shekel prices |
| Skyscanner | `https://www.skyscanner.co.il/transport/flights/tlv/{dest}/{YYMMDD}/{YYMMDD}/` | Lowercase airport code (e.g. `ath`); dates as `YYMMDD`. For a whole month or "Everywhere", use the options on the search form; do not guess those URLs |
| KAYAK | `https://il.kayak.com/flights/TLV-{DEST}/{YYYY-MM-DD}/{YYYY-MM-DD}?sort=price_a` | IATA codes; `sort=price_a` = cheapest first; use `il.kayak.com` for a Hebrew/ILS view |

- One-way: drop the second date segment on Skyscanner and KAYAK.
- Nonstop and max-price filters: apply them on the results page (sidebar), do not fabricate filter query parameters.
- All three platforms, KAYAK included, render fares with JavaScript, so read them with a real browser/rendering tool or a flights MCP; a plain WebFetch returns an empty shell with no fares.
- Every template opens for 1 adult: set the full passenger mix (adults, children with ages, infants) on each platform's search form before reading prices, and do not guess passenger query parameters.
- Worked example (TLV→Athens, 6-11 Dec 2026): Skyscanner `.../tlv/ath/261206/261211/`; KAYAK `.../TLV-ATH/2026-12-06/2026-12-11?sort=price_a`.

## Platforms

Feature sets change; treat these as roles in the workflow, not guarantees, and confirm on the site.

| Platform | URL | Role in this workflow |
|----------|-----|-----------------------|
| Google Flights | google.com/travel/flights?gl=IL&hl=he | First look at airline prices; "Explore" map for flexible destinations; price tracking |
| Skyscanner | skyscanner.co.il | Cross-check including OTA prices; "Everywhere" and whole-month views |
| KAYAK | il.kayak.com | Second cross-check; price alerts |
| Issta | issta.co.il | Israeli agency for flight+hotel packages and human help in Hebrew |
| Lametayel | lametayel.co.il | Israeli travel site with a flight search |

## Quick Picks

| Need | Start with |
|------|------------|
| Cheapest flight overall | Google Flights + Skyscanner cross-check |
| Cheapest destination for my dates | Skyscanner "Everywhere" or Google Flights "Explore" |
| Flight + hotel package | Issta |
| Price drop alerts | Google Flights or KAYAK |
| Hebrew-only user who wants a person to help | Issta |
