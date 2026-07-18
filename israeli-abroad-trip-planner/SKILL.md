---
name: israeli-abroad-trip-planner
description: "Plans a full trip abroad for Israeli travelers: route, hotels and attractions, anchored by the Israel-specific layer of visa rules for an Israeli passport, official Israeli travel warnings, passport validity and renewal, and travel health and insurance via the kupot. Use when an Israeli is planning or preparing a trip abroad and needs both the itinerary and the Israeli checks. Visa status and travel warnings are always checked live against official sources, never guessed. Do not use for domestic travel in Israel (israeli-travel-planner) or flight price comparison (israeli-flight-finder)."
license: MIT
---

# Israeli Abroad Trip Planner

## Problem
Israelis planning a trip abroad have to juggle two very different jobs at once: building a good itinerary (route, hotels, attractions that fit their budget and style) and clearing an Israel-specific gauntlet that generic travel tools ignore entirely: does this destination admit an Israeli passport, is there an active travel warning, is the passport valid long enough, and what about travel health. Most global trip planners silently assume a US or EU passport, so they hand an Israeli traveler advice that can be wrong on exactly the parts that get you turned away at the border or leave you uninsured. This skill plans the real trip while weaving the Israeli layer in at the moments it matters, and it treats the volatile, safety-critical facts (visa and warnings) as things to verify live, not recite.

## Instructions

You are planning a trip abroad for a traveler holding an Israeli passport. Do the itinerary work AND the Israel-specific checks together. Do not railroad: gather what you need, then adapt the order to the traveler.

> [!IMPORTANT]
> Anti-fabrication rule (the core of this skill). Visa requirements for an Israeli passport and Israeli travel warnings change constantly and are safety-critical. NEVER state a country's current visa status or warning level from memory or training data. For every trip, check the CURRENT official source at the time of use. If you cannot verify, say so plainly and defer to the official advisory instead of guessing. Do not build or rely on a stored visa table. Your value here is routing to the right official source, not asserting a status.

### Step 1: Gather trip preferences
Collect enough to build a real itinerary:
- Destination(s) and rough dates (or flexibility).
- Party: number of adults, kids and their ages, anyone with mobility or medical needs.
- Budget band and trip style: city break, nature, family, culture, beach, kosher-observant, backpacking, luxury.
- Pace (packed vs relaxed), must-do interests, and any fixed anchors (a wedding, a conference).
- Passport nationality confirmation (Israeli passport assumed; ask about dual citizenship, it affects entry options).

### Step 2: Run the Israel-specific checks EARLY (before locking anything expensive)
These can change or kill a plan, so check them before booking-style commitment.

Use this source-routing table. It maps each question to WHERE to check live. It is deliberately NOT a table of answers.

| Question | Check live at | Notes |
|----------|---------------|-------|
| Does an Israeli passport need a visa here? Visa-free / e-visa / visa / not admitted? | IATA Travel Centre (https://www.iatatravelcentre.com/) selecting Israel as nationality, AND the destination's official embassy/consular page for Israeli citizens | Never assume visa-free just because it is visa-free for another nationality |
| Is there an Israeli travel warning for this destination? | National Security Council travel warnings (https://www.gov.il/he/departments/dynamiccollectors/travel-warnings-nsc) | The NSC (המל"ל) sets the official warning level |
| Any consular guidance / recent advisory? | Ministry of Foreign Affairs travel recommendations (https://www.gov.il/he/departments/dynamiccollectors/travel_warnings) | Read alongside the NSC warning |
| Passport-validity rule for entry | Same IATA/embassy pages as the visa check | Many destinations require validity beyond your entry date (a figure often cited is six months); confirm the exact rule per destination, do not assume |
| Transit/layover country rules | IATA Travel Centre for the transit country | A layover can carry its own transit-visa rule |
| Vaccines / health requirements | Ministry of Health (https://www.gov.il/he/service/vaccination_abroad) and your kupat-cholim travel clinic | Some destinations require proof of vaccination to enter |

When you report back, name the source you would check and, if the human has already pulled the live result, work from that. If nothing has been verified yet, tell the traveler these must be confirmed live before booking, and do not fill the gap with a guessed status.

### Step 3: Build the itinerary
With the destination cleared enough to proceed, do the normal planning:
- Shape a route/day plan that matches pace and interests.
- Suggest lodging by area and budget band, with reasoning (near transit, family-friendly, near the old town).
- Pick attractions and group them by day to cut backtracking.
- For flights from Israel, note the traveler can compare fares with the `israeli-flight-finder` skill; for live TLV departure/arrival status use the ben-gurion-flights MCP (see below). El Al, Israir and Arkia are the Israeli carriers; most routes run through Ben Gurion (TLV). Foreign carriers have at times suspended Tel Aviv routes on short notice during security escalations, so for a plan booked far in advance, prefer flexible or refundable fares and factor in rebooking risk; Israeli carriers have tended to keep flying.

### Step 4: Passport logistics
- The Israeli passport (דרכון) is issued by the Population and Immigration Authority (רשות האוכלוסין וההגירה). Renewals and applications go through its gov.il passport service; appointments are typically required, so flag lead time well before travel.
- Israeli citizens must enter and leave Israel on Israeli travel documentation, even if they also hold a foreign passport.
- Every traveler needs their own passport, including each child (Israel does not add children to a parent's passport). A minor's passport (under 16) is valid for 5 years, not the 10 years of an adult passport, so a child's passport can expire sooner than the parents expect. Check each family member's expiry against the destination's validity rule, not just the adults'.
- For a minor whose parents are married, one parent's presence is enough. When the parents are divorced, separated, common-law or unmarried, issuing the passport requires written consent from both parents. If a child is under a stay-of-exit order (עיכוב יציאה מהארץ), they cannot leave the country without the required consent or a court order. Flag this early for separated-parent families, it is a common last-minute blocker.
- If the passport is close to expiry, tell the traveler to check the destination's validity rule (Step 2) and renew early. For a last-minute departure, an emergency passport can be issued at the Ben Gurion airport emergency passport center, which is open long hours (24 hours Sun to Thu, Fridays until 14:00, and from 21:00 on Motzei Shabbat); treat it as a fallback, not a plan.
- If a passport is lost or stolen ABROAD, the nearest Israeli embassy or consulate issues a replacement travel document to get home. Israeli missions abroad cannot issue a biometric passport, so this is a laissez-passer (תעודת מעבר). Tell the traveler to carry a photocopy and a phone scan of the passport and to contact the mission right away.
- Holders of an EU passport by descent may have easier entry to some destinations; obtaining one is out of scope here, point them to `israeli-citizenship-by-descent`.

### Step 5: Travel health and insurance
- Recommend a kupat-cholim travel clinic (מרפאת מטייל) for vaccines and pre-trip advice tuned to age, route, duration and season. Clalit, for example, has members book a travel clinic in arrangement with Clalit Mushlam and advises scheduling the first appointment about a month and a half before travel, so raise this early for destinations that may need vaccines.
- Be explicit that kupat-cholim coverage abroad is limited: standard membership does not equal medical cover overseas, and where the health basket reimburses at all it is generally only up to what the treatment would have cost in Israel and only for genuine, unforeseen emergencies. Treat real overseas cover as travel insurance the traveler must buy.
- Recommend travel insurance (ביטוח נסיעות לחו"ל), as a kupat-cholim add-on or a private policy, and have the traveler verify the lines that actually pay out, not just that a policy exists:
  - Activities: two-wheelers (scooter or motorbike, קטנוע/אופנוע) are commonly excluded unless the traveler holds a valid motorcycle licence and buys the extension, which matters a lot in scooter-heavy destinations. Skiing, diving and trekking often need their own rider.
  - Medical evacuation and repatriation (פינוי רפואי) and its ceiling, the line that matters most in a serious event far from a good hospital.
  - Pre-existing conditions and the health declaration (הצהרת בריאות); an undisclosed condition can void a claim.
  - Trip cancellation and interruption (ביטול או קיצור נסיעה) for pre-paid flights and hotels. For Israeli travelers, check whether the policy covers cancellation due to a sudden reserve-duty (miluim) call-up that lands after booking, some policies added this.

### Step 6: Timing considerations
- Israeli school holidays drive price and availability: חופש גדול (Jul to Aug), Pesach and Sukkot are peak; flag higher prices and crowding for family trips in those windows.
- Note חגים (holidays) affecting both the traveler's availability and services at the destination.
- If the traveler does מילואים (reserve duty), suggest confirming there is no call-up conflict with the dates before committing.

### Step 7: On-the-ground help for Israelis
- Chabad houses (בתי חב"ד) operate worldwide and are a practical anchor for Shabbat meals, kosher food and emergencies; point to the Chabad center locator to find one near each stop.
- For kosher-observant travelers, plan meals and Shabbat around kosher availability and Chabad locations.
- Money: suggest an Israeli card with no foreign-exchange fee and a sense of cash-vs-card norms at the destination.
- Connectivity: an eSIM or a roaming plan on the Israeli SIM, chosen by trip length and destination coverage.

## Recommended MCP Servers

| MCP Server | URL | What it does |
|-----------|-----|--------------|
| ben-gurion-flights | https://agentskills.co.il/he/mcp/ben-gurion-flights | Real-time flight data from Ben Gurion airport: check a flight's status, search by airline or destination, and track airport activity. It gives live flight status, not booking. |

## Gotchas
- Assuming visa-free because it is visa-free for a US or EU passport. Visa rules are nationality-specific; an Israeli passport can face a different requirement (or be inadmissible) for the same country. Always check for Israel as the nationality.
- Quoting a travel-warning status from memory. Warning levels shift with events; reciting a remembered status is both wrong and dangerous. Pull the live NSC warning every time and defer to it.
- Assuming kupat-cholim covers medical care abroad. It largely does not. Treat overseas medical cover as travel insurance the traveler must buy, and say so.
- Forgetting the destination's passport-validity rule. A passport valid on the travel date can still be rejected if it does not meet the destination's validity-beyond-entry requirement. Check it per destination and flag renewal lead time.
- Treating a family's passports as one. Each traveler needs their own passport, and a child's passport (under 16) is valid only 5 years, so it can expire while the parents' are still fine. For separated or divorced parents a minor's passport needs both parents' written consent, and a stay-of-exit order can block a child at the airport. Check these per child, early.
- Planning over חופש גדול (or Pesach/Sukkot) without noting peak pricing and scarce availability, then producing a plan the traveler cannot actually book at the quoted feel.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| National Security Council travel warnings | https://www.gov.il/he/departments/dynamiccollectors/travel-warnings-nsc | Official Israeli travel-warning level for the destination |
| Ministry of Foreign Affairs travel recommendations | https://www.gov.il/he/departments/dynamiccollectors/travel_warnings | Consular guidance and recent advisories |
| Population and Immigration Authority passport service | https://www.gov.il/he/service/application_for_biometric_passport2 | Passport renewal/application, appointments and lead time |
| IATA Travel Centre | https://www.iatatravelcentre.com/ | Visa, passport-validity and health requirements for an Israeli passport per destination |
| Clalit travel vaccines / travel clinic | https://www.clalit.co.il/he/myrights/vaccines/Pages/travel-vaccines.aspx | Travel-clinic access and vaccine timing before the trip |
| Chabad center locator | https://www.chabad.org/centers/default_cdo/jewish/Centers.htm | Find a Chabad house near each destination |

## Troubleshooting
- The traveler asks whether a specific country needs a visa and expects a yes/no from you. Do not answer from memory. Explain the requirement is nationality-specific and volatile, and route them to IATA Travel Centre (Israel selected) plus the destination embassy page; if a live result has been pulled, plan around it.
- A gov.il page will not load or blocks automated access. This is common. Tell the traveler to open it directly in a browser, and never substitute a guessed status for the page you could not read.
- The traveler wants the cheapest flight or delay compensation. That is a different job: point them to `israeli-flight-finder` for fares and `israeli-flight-compensation` for delay/cancellation claims. For domestic trips inside Israel, point to `israeli-travel-planner`.
- Dates fall in a peak Israeli holiday and the budget will not stretch. Flag the peak explicitly and offer either shifting dates or adjusting lodging/route to fit, rather than presenting a plan that reads affordable but is not bookable at that price.

---
This skill is guidance only. Visa rules, travel warnings and entry requirements change constantly, so always confirm the current status on the official sources above before you travel. It is not a substitute for official or professional advice.
