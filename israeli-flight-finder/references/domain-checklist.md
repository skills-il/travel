# Domain Coverage Checklist: Israeli Flight Finder

Scope: helping a traveler in Israel find and compare the cheapest international flights from Ben Gurion (TLV) / Ramon (ETM), including doing the live comparison, understanding Israeli-airline pricing, and clearing entry/scheduling constraints.

## Must cover (core)

- **Live comparison workflow**: build pre-filled search links for the exact route and dates, pull the actual current fares, normalize to total cost, and present a real comparison. This is the skill's core job. (Precedent: user complaint that a "flight finder" that only names websites without comparing is not usable.)
- **Comparison platforms**: Google Flights, Skyscanner, KAYAK (global, Hebrew UI) + Issta / Lametayel (Israeli agencies, packages). What each is best for.
- **Deep-link / pre-filled search URLs** for the platforms so a search can be constructed programmatically (Google Flights `q=` NL query, Skyscanner `/transport/flights/tlv/{dest}/{YYMMDD}/`, KAYAK `/flights/TLV-{DEST}/{date}/`).
- **Anti-fabrication rule for prices**: fares change hourly; never invent or recall a price. If live data cannot be read, hand over the pre-filled links. (Core trust requirement.)
- **Israeli carriers**: El Al (LY), Israir (6H), Arkia (IZ), plus low-cost (Wizz Air) and the foreign-carrier landscape. Network scope and hub (TLV / Ramon).
- **Baggage policies + fees** for El Al (Lite/Classic/Flex), Israir, Arkia, Wizz, incl. advance-vs-airport pricing and the El Al Lite Europe/UAE gate-check rule. Baggage must be folded into total-cost comparison. (2026-10-25: Arkia's fee table was removed because arkia.co.il blocks automated reading and the figures could not be re-verified; the skill routes Arkia fees to its booking flow. Re-add a table only after reading the live page in a real browser session.)
- **Shabbat-aware scheduling**: El Al does not fly Shabbat or Yom Tov days (Hanukkah, Purim, Chol HaMoed are not rest days); Israir and Arkia fly on Shabbat as of May 2026 (Israir under Haredi boycott pressure, verify); foreign carriers: check the route runs on the needed day. (Israeli-calendar constraint generic tools ignore.)
- **Seasonal pricing**: peak (chagim incl. Hanukkah, summer, Christmas/New Year, Purim), shoulder, off-peak (January after the New Year wave); holiday prices climb in the weeks before (stated qualitatively: no sourced figure for the lead time). Dated upcoming holidays from hebcal (Israel), refreshed each cycle.
- **Entry requirements for Israeli travelers**: passport validity (6 months common; Schengen 3 months + issued within 10 years; minors under 16 get 5-year passports), passport issue timing (~6 weeks, temporary passport only at Ben Gurion within 48h), EES (fully operational 10 April 2026), ETIAS (not operating, no launch date announced as of October 2026), UK ETA (required since 8 January 2025), US ESTA (e-Passport required), Canada eTA, NSC travel warnings. A cheap fare is worthless if the traveler cannot board/enter. (Added UK/US/Canada 2026-10-25 after an aggregator sweep found them missing.)
- **TLV security / arrival time**: Israel Airports Authority 3-hours-before-international recommendation.
- **Volatility disclaimer**: post-Feb-2026-war carrier status is a moving target; verify live per airline/route. Dated snapshot in references/tlv-carrier-status.md.
- **Passenger mix and party total** (added 2026-10-25): ask adults, each child's age, lap infants; set the mix on the platform rather than guessing URL parameters; total = sum over passengers and directions of fare + bags + seats; never compute a child discount from memory.
- **Passenger rights pointer** (added 2026-10-25): Israeli Aviation Services Law rights on cancelled/delayed flights to/from Israel, routed to israeli-flight-compensation; self-transfer separate tickets refund only the cancelled segment.
- **Where to buy** (added 2026-10-25): prefer airline or Israeli agency over unknown foreign OTAs when prices are close; refund handling in mass cancellations sits with the seller.

## Should cover (advanced)

- **Booking strategy / timing**: book weeks not months out; day-of-week effects small; use price alerts (Google Flights / KAYAK).
- **Money-saving tactics**: cross-check 3+ platforms, flexible dates (whole-month view), nearby airports, multi-city / open-jaw, Skyscanner "Everywhere".
- **Israeli deal sources**: secret-flights sites, Telegram/Facebook deal channels (error fares not on aggregators).
- **Points & miles**: El Al Matmid, Israeli credit-card earn (Isracard, Amex IL, Max).
- **Flight+hotel packages**: Issta / Lametayel bundles vs booking separately.
- **Kosher / special meals**: El Al kosher by default; foreign carriers need KSML request.
- **Disruption protection**: refundable fares / insurance covering airspace closure (2026 TLV risk).
- **Recommended MCP**: Ben Gurion Flights (live TLV arrivals/departures, flight status, not prices).

## Must cover (added 2026-07-29)

- **Currency normalization** - every figure entering the NIS comparison table (Israir USD baggage tables, any USD-quoting search MCP) must be converted using a rate read in-session, with the ~3% Israeli card foreign-currency conversion fee included in the ranked total. Source: max.co.il abroad-commissions.
- **Third-party flight-search MCP governance** - when a non-skills-il MCP supplies prices, the skill must state the source per row, disclose single-source results rather than implying full market coverage, prefer the offer's own baggage data, and forbid both the booking tool and referral to that vendor as a purchase venue.
- **Foreign-seller consumer exposure** - surfacing a foreign reseller's fare must flag that Israeli consumer-protection cancellation rules may not be available against it, and where its terms impose a foreign governing law or arbitration forum (Rift, formerly Soar: Delaware law, JAMS arbitration in Wilmington, checked 2026-10-25), say so.

## Out of scope (explicit)

- **Departure airport choice (TLV vs Ramon/Eilat)** - moved here 2026-10-25: no post-war (after February 2026) source for Ramon's current international or charter routes could be found, so the skill makes no claim about it rather than an unsourced one. Re-add under Should cover once an IAA or airline source confirms current Ramon international routes.

- **Domestic travel within Israel** - handled by `israeli-travel-planner`.
- **Train schedules** - handled by `railil`.
- **Hotel-only bookings** - not a flight-comparison task.
- **Actual booking / payment execution** - the skill compares and links out; the traveler books on the platform. Reaffirmed 2026-07-29: this now explicitly extends to third-party booking MCPs. The skill may call a flight-search MCP for prices but must never invoke its booking tool nor route the traveler to it to buy.
- **Live price data as a stored fact** - prices are pulled live per query, never encoded in the skill. Reviewed 2026-10-25: users ask "how much is it usually?", but any stored fare would be wrong within hours, so this stays out.
- **Hotel-only, car rental, airport parking, pets, unaccompanied minors** - reviewed 2026-10-25: users do ask these next, but they are not flight-price comparison. Packages (flight+hotel) stay in scope via Issta/Lametayel; the rest is out of scope and the agent should say so rather than improvise.
- **Exact passenger-count URL parameters** - reviewed 2026-10-25: could not be verified from any official source (KAYAK and Skyscanner serve bot checks; no public spec), so the skill tells the agent to set passengers on the search form instead of guessing parameters.
- **Shabbat-flying permanence (Israir, Arkia)** - reviewed 2026-10-25. A user would ask "who flies Saturday night?"; the body answers it with a dated status (May 2026) and tells the agent to verify live. Watch items: Haredi boycott pressure on Israir (May 2026); February 2026 talks to sell Arkia control to a US investor, no closed deal found. The no-source "Haredi buyout" wording was dropped.

## Authoritative sources

- Airline baggage/network: elal.com/eng/baggage, israir.co.il, arkia.co.il/en/luggage-information, wizzair.com
- Carrier resumption status (post-war): airline own sites; travel trade press (mtm.travel, openjaw.com), ynetnews, timesofisrael
- Entry rules: travel-europe.europa.eu (EES/ETIAS), home-affairs.ec.europa.eu, gov.uk/eta, cbp.gov / esta.cbp.dhs.gov, canada.ca, kolzchut.org.il (passports), gov.il NSC travel warnings
- Holiday dates: hebcal.com (Israel schedule, yomtov flag)
- TLV security: iaa.gov.il
- Platforms: google.com/travel/flights, skyscanner.co.il, kayak.com, issta.co.il, lametayel.co.il
