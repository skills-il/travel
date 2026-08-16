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
- Passport logistics: Israeli passport issued by the Population and Immigration Authority (רשות האוכלוסין וההגירה); destination passport-validity requirement (verify per destination, do not assert globally); renewal path (appointment-only, six-week issuance, reduced fee Nov to end Feb); emergency passport (דרכון חירום, valid 1 year) at 17 Population Authority bureaus as well as Ben Gurion; and what a mission abroad actually issues after a loss (a NON-biometric Israeli travel document, not a תעודת מעבר).
- Travel health: kupat-cholim travel clinic (מרפאת מטייל) for vaccines/advice, timing ahead of travel; travel insurance (ביטוח נסיעות) as a kupat-cholim add-on vs private policy; kupat-cholim coverage abroad is limited.
- Timing: Israeli school holidays (חופש גדול Jul-Aug, Pesach, Sukkot), חגים, מילואים considerations and their effect on price/availability.
- On-the-ground for Israelis: Chabad houses (בתי חב"ד) worldwide, kosher food, El Al / Israir / Arkia and Ben Gurion (TLV) routing, no-FX-fee Israeli cards, eSIM/roaming.
- Explicit anti-fabrication rule: visa + warnings MUST be checked live against official sources every time; if unverifiable, say so and defer to the official advisory.
- Electronic travel authorizations as a CATEGORY distinct from visas (UK ETA, US ESTA, and the same-shaped schemes in Canada, New Zealand, South Korea, Thailand). Named because they are stable and knowable, unlike per-country visa status, and because missing one means denied boarding rather than a border problem. ETIAS is flagged as pending with no confirmed launch date.
- Exit restrictions (עיכוב יציאה מהארץ) for ADULTS as well as minors, including the Execution Office (הוצאה לפועל) debt route, and how to check in advance.
- New olim: the first-year תעודת מעבר and when passport entitlement begins.
- Consular emergency channel: the MFA situation room, the mission locator, and the medical-emergency call order through the insurer's assistance company.
- Prescription and controlled medication crossing borders.
- Travel-insurance failure modes that void claims, not just the rider list: buy-before-departure, travel-warning-destination exclusion, pregnancy and age limits.

## Should cover (advanced)
- Which official source answers which question (a source-routing table, not an answer table).
- Transit/layover visa and authorization checks (a stop in a third country can need its own rule).
- Entry stamp / prior-travel sensitivities relevant to Israeli passports for some destinations.
- Family-with-kids specifics: minors' passports, and the SEPARATE destination-side notarial consent when a minor travels alone or with one parent.
- Dual nationality as a liability as well as an advantage (subject to the other state's laws, including conscription, on its territory).
- EU Entry/Exit System and machine-enforced 90/180 counting at Schengen borders.
- National Insurance consequences of long stays abroad (health-entitlement waiting period on return).
- International driving permit when the itinerary includes car rental.
- Money: FX-fee-free Israeli cards, cash vs card norms at destination.
- Connectivity: eSIM vs roaming for an Israeli SIM.
- Cross-links to related skills at the right moments.
- A no-browsing branch: what to deliver, and how to hand a lookup to the human, on hosts that cannot fetch.

## Out of scope (explicit)
- Domestic travel inside Israel: use `israeli-travel-planner`.
- Flight price comparison / cheapest-fare hunting from Israel: use `israeli-flight-finder`.
- Flight delay / cancellation compensation claims: use `israeli-flight-compensation`.
- Obtaining an EU passport by descent: use `israeli-citizenship-by-descent`.
- Booking/payment execution (the skill plans and routes; it does not transact).
- Asserting a specific country's current visa status or warning level from memory (forbidden by design).
- Pet relocation / flying with animals. Reviewed 2026-08-16: a real adjacent need, but it is a separate multi-month veterinary process (Ministry of Agriculture Veterinary Services, rabies antibody testing). Out of scope with a pointer, not covered.
- Exit tax / severance of tax residency (s.100A of the Income Tax Ordinance). Reviewed 2026-08-16: a capital-gains matter on ceasing residency, not a trip-planning matter. A "travel levy" (מס נסיעות) was searched for in this cycle and NO authoritative source on its current status was found, so nothing is asserted about it either way.
- Customs personal exemption on return. Reviewed 2026-08-16: an ordinary user would plausibly ask, so this is a genuine re-open candidate, but the commonly-cited figure could not be confirmed against a רשות המסים primary source in this cycle and the skill will not publish an unverified allowance. Carried to the next cycle.
- IDF exit clearance procedure for draft-age travelers. Reviewed 2026-08-16: the CONSTRAINT is surfaced in Step 6 as a "confirm with your enlistment office" item, but the procedure itself is deliberately not stated because no primary source could be reached this cycle. Carried.

## Authoritative sources
- National Security Council travel warnings: https://www.gov.il/he/departments/dynamiccollectors/travel-warnings-nsc
- Ministry of Foreign Affairs travel recommendations: https://www.gov.il/he/departments/dynamiccollectors/travel_warnings
- Population and Immigration Authority passport service: https://www.gov.il/he/service/application_for_biometric_passport2
- Ministry of Health vaccination for travelers abroad: https://www.gov.il/he/service/vaccination_abroad
- MFA situation room (24/7): https://www.gov.il/he/pages/matzav
- MFA visa-exemption table for Israeli passports: https://www.gov.il/BlobFolder/reports/examption_visa-israeli-heb/he/ISR_Visa_Abroad_Heb.pdf
- Leaving Israel with minors (notarial consent): https://www.gov.il/he/pages/leaving_the_country_with_minors
- Emergency (temporary) passport: https://www.gov.il/he/pages/temporary_passports
- Cancelling a stay-of-exit order: https://www.gov.il/he/service/exit_order_cancel_stay
- UK ETA: https://www.gov.uk/eta
- US ESTA: https://esta.cbp.dhs.gov/
- EU Entry/Exit System: https://home-affairs.ec.europa.eu/policies/schengen/smart-borders/entry-exit-system_en
- National Insurance waiting period after a long stay abroad: https://www.btl.gov.il/Insurance/Living_abroad/Pages/chishuvTkufatHamtana.aspx
- International driving permit stations: https://www.gov.il/he/departments/dynamiccollectors/photo_driving_license_stock
- Clalit travel vaccines / travel clinic: https://www.clalit.co.il/he/myrights/vaccines/Pages/travel-vaccines.aspx
- IATA Travel Centre (passport/visa/health by nationality): https://www.iatatravelcentre.com/
- Chabad center locator (worldwide): https://www.chabad.org/jewish-centers/
- ben-gurion-flights MCP (live TLV flight status): https://agentskills.co.il/he/mcp/ben-gurion-flights

## Aggregator sweep note
Aggregators (Kol Zchut, Chaim V'Chessed, the MFA consular hub) are useful for orientation but are NOT authoritative for visa/warning status. Always confirm the visa and warning against the primary official source at use-time. Reachability, checked 2026-08-16: gov.il, kolzchut.org.il, chabad.org and iatatravelcentre.com all return HTTP 403 to plain fetches while rendering normally in a real browser, and IATA additionally shows a Cloudflare security check. A 403 from these hosts is therefore NOT evidence that a page is dead or a requirement changed; re-check in a browser before ever removing a citation. A human or a browsing-capable agent should open them live rather than trust a cached summary.

## Domain checklist version 2 (2026-08-16)
Version 1 was written against a skill that treated the Israeli layer as visa + warning + passport + health. This cycle found that framing too narrow: the failures that actually strand Israeli travelers are an adult exit order, a missing electronic authorization, and a wrong document after a loss abroad. Those are now Must-cover rows.
