# Domain Checklist: Israeli Abroad Trip Planner

Contract the SKILL.md is judged against. Slug: `israeli-abroad-trip-planner`. Category: `travel`.
Audience: Israelis (Israeli passport holders) planning a trip abroad (chul).

## Design premise
This is a full trip planner (route, hotels, attractions) whose differentiator is the Israel-specific layer. Visa status for an Israeli passport and official travel warnings are safety-critical AND change constantly, so the skill's core value is orchestrating the RIGHT live official source per question, never asserting a volatile status from memory.

## Must cover (core)
- Preference gathering to build the actual trip: destination(s), dates, budget, party (adults/kids/ages), trip style (city/nature/family/culture/kosher-observant), pace, must-do interests.
- Route + itinerary shaping, lodging guidance, attraction selection tuned to the stated preferences.
- Visa requirement CHECK for the Israeli passport per destination, framed as a live-lookup, never a hardcoded table. Route to IATA Travel Centre and the destination country's official consular/embassy page for Israeli citizens.
- Official Israeli travel-warning CHECK: National Security Council (המטה לביטחון לאומי / המל"ל) travel warnings + Ministry of Foreign Affairs consular guidance. Live lookup every time.
- Passport logistics: Israeli passport issued by the Population and Immigration Authority (רשות האוכלוסין וההגירה); destination passport-validity requirement (verify per destination, do not assert globally); renewal path; emergency passport (דרכון חירום) at Ben Gurion.
- Travel health: kupat-cholim travel clinic (מרפאת מטייל) for vaccines/advice, timing ahead of travel; travel insurance (ביטוח נסיעות) as a kupat-cholim add-on vs private policy; kupat-cholim coverage abroad is limited.
- Timing: Israeli school holidays (חופש גדול Jul-Aug, Pesach, Sukkot), חגים, מילואים considerations and their effect on price/availability.
- On-the-ground for Israelis: Chabad houses (בתי חב"ד) worldwide, kosher food, El Al / Israir / Arkia and Ben Gurion (TLV) routing, no-FX-fee Israeli cards, eSIM/roaming.
- Explicit anti-fabrication rule: visa + warnings MUST be checked live against official sources every time; if unverifiable, say so and defer to the official advisory.

## Should cover (advanced)
- Which official source answers which question (a source-routing table, not an answer table).
- Transit/layover visa checks (a stop in a third country can need its own transit rule).
- Entry stamp / prior-travel sensitivities relevant to Israeli passports for some destinations.
- Family-with-kids specifics: minors' passports, consent-to-travel considerations.
- Money: FX-fee-free Israeli cards, cash vs card norms at destination.
- Connectivity: eSIM vs roaming for an Israeli SIM.
- Cross-links to related skills at the right moments.

## Out of scope (explicit)
- Domestic travel inside Israel: use `israeli-travel-planner`.
- Flight price comparison / cheapest-fare hunting from Israel: use `israeli-flight-finder`.
- Flight delay / cancellation compensation claims: use `israeli-flight-compensation`.
- Obtaining an EU passport by descent: use `israeli-citizenship-by-descent`.
- Booking/payment execution (the skill plans and routes; it does not transact).
- Asserting a specific country's current visa status or warning level from memory (forbidden by design).

## Authoritative sources
- National Security Council travel warnings: https://www.gov.il/he/departments/dynamiccollectors/travel-warnings-nsc
- Ministry of Foreign Affairs travel recommendations: https://www.gov.il/he/departments/dynamiccollectors/travel_warnings
- Population and Immigration Authority passport service: https://www.gov.il/he/service/application_for_biometric_passport2
- Ministry of Health vaccination for travelers abroad: https://www.gov.il/he/service/vaccination_abroad
- Clalit travel vaccines / travel clinic: https://www.clalit.co.il/he/myrights/vaccines/Pages/travel-vaccines.aspx
- IATA Travel Centre (passport/visa/health by nationality): https://www.iatatravelcentre.com/
- El Al official site: https://www.elal.com/en
- Chabad center locator (worldwide): https://www.chabad.org/centers/default_cdo/jewish/Centers.htm
- ben-gurion-flights MCP (live TLV flight status): https://agentskills.co.il/he/mcp/ben-gurion-flights
- Nefesh B'Nefesh passport guide (aggregator context): https://www.nbn.org.il/life-in-israel/government-services/obtaining-an-israeli-passport/

## Aggregator sweep note
Aggregators (Nefesh B'Nefesh, Chaim V'Chessed, tlvflights threat-map mirrors) are useful for orientation but are NOT authoritative for visa/warning status. Always confirm the visa and warning against the primary official source at use-time. gov.il pages frequently block automated fetching; a human/agent should open them live rather than trust a cached summary.
