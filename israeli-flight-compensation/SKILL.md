---
name: israeli-flight-compensation
description: >-
  Determines whether an air passenger is owed compensation under Israel's Aviation Services Law
  (חוק שירותי תעופה, 2012, "חוק טיבי") and drafts a Hebrew demand letter to the airline. Use when
  a flight to or from Israel was cancelled, delayed, overbooked, downgraded, or moved earlier, and
  the user asks "am I owed compensation", "pitzuy al bitul tisa", "ta'osa hit'akva", "the airline
  cancelled my flight", or wants to claim without paying a claim-handling service a cut. Calculates
  the amount by distance band (2026 figures), explains assistance rights, and routes refusals to
  small claims. Do NOT use for booking flights (use israeli-flight-finder), lost or damaged baggage
  (Montreal Convention), travel insurance, or flights with no Israeli departure or arrival.
license: MIT
allowed-tools: 'Bash(python3:*)'
compatibility: >-
  Pure-knowledge plus a Python helper script (no network needed for the calculation). Works with
  Claude Code, Claude.ai, Cursor, and other listed agents.
---

# Israeli Flight Compensation

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Problem

Israeli passengers are owed real money when a flight to or from Israel is cancelled, badly delayed, or overbooked, but most people never claim it, and those who do often hand a large success fee to a claim-handling service for a letter they could send themselves. The rights come from Israel's own Aviation Services Law (חוק טיבי), which is different from the European rules people half-remember, with different amounts and a different delay threshold. This skill works out exactly what the law owes the passenger and writes the demand letter for free.

## Instructions

You help a passenger determine their entitlement under the Aviation Services Law (Compensation and Assistance for Flight Cancellation or Change of Conditions), 2012, and produce a demand letter. Read `references/compensation-table.md` for the full rate table and thresholds before quoting any figure.

### Step 1: Confirm the law even applies (scope gate)

The Aviation Services Law applies only to a flight that departs from Israel OR arrives to Israel (including itineraries with a stopover), on any carrier, Israeli or foreign. Domestic Israeli flights are covered under separate regulations with a 3-hour threshold.

If the flight neither departs from nor arrives to Israel, STOP and tell the user this law does not apply; EU Regulation 261/2004 may cover it instead, with different amounts (250/400/600 EUR) and a 3-hour delay threshold. Never quote the Israeli amounts for a non-Israel flight, and never quote EU261 amounts as if they were the Israeli entitlement. The two regimes are separate, but they do OVERLAP on many Israel routes, so do not treat "the Israeli law applies" as meaning EU261 cannot. Step 6.5 has the test and the claiming order.

**Then check the ticket itself.** Entitlement attaches to a passenger who was ISSUED a ticket and presented for check-in on time. Two ticket types are excluded from all benefits under section 2(b)(2): a ticket received free of charge, and a ticket bought at a special fare not available to the public directly or indirectly (staff tickets, industry discounts, negotiated non-public fares). The carve-back matters and is the common case: a ticket issued under a frequent-flyer or loyalty programme IS covered, so an award ticket bought with points is a full claim. Ask how the ticket was obtained before quoting any amount, and note that a lap infant with no issued ticket of their own has no entitlement.

### Step 2: Classify the disruption

Ask what happened and map it to one trigger:

- Cancellation: the airline cancelled. Compensation is owed when notice was less than 14 days before departure AND no qualifying alternative was offered. "Qualifying" is defined by how much notice was given, and it is the carrier's most common defence, so check it rather than assuming:
  - 7 to 14 days notice: no compensation if the alternative departs no more than 2 hours early AND arrives no more than 4 hours late.
  - Less than 7 days notice: no compensation if the alternative departs no more than 1 hour early AND arrives no more than 2 hours late.
  Assistance and the refund-or-alternative choice still stand either way.
- Delay treated as cancellation: the flight departed 8 or more hours late (international), or 3 or more hours late (domestic).
- Denied boarding (overbooking): the passenger was bumped and did NOT volunteer to give up the seat.
- Early departure: moved earlier by more than 5 and up to 8 hours with less than 14 days notice gives a refund or an alternative flight; moved earlier by more than 8 hours adds the monetary compensation on top.
- Downgrade: the passenger was moved to a lower class than booked.

### Step 3: Gather the inputs for the amount

Collect: the origin and final destination (to get the distance band), the length of the delay, how much notice the airline gave, whether the passenger accepted an alternative flight and how late that alternative arrived versus the original, and the flight date (to check it against the closed Iron Swords windows listed in Step 5, and against any emergency order that was in force on that date).

### Step 4: Compute the entitlement

Use the figures in `references/compensation-table.md`, or run the helper for a clean breakdown:

```bash
python3 scripts/compensation_calc.py --distance-km 3000 --delay-hours 9
python3 scripts/compensation_calc.py --distance-km 6000 --delay-hours 9 \
    --alternative-accepted --alternative-arrival-delay-hours 3
python3 scripts/compensation_calc.py --distance-km 9000 --delay-hours 9 --passengers 4
python3 scripts/compensation_calc.py --domestic --domestic-route eilat --delay-hours 4
```

Domestic flights do NOT use the distance bands. Section 18 defers them to separate regulations with their own amounts: 300 NIS on the Eilat routes, 180 NIS on Sde Dov to Ein Yahav or Rosh Pina, and 240 NIS on any other domestic route (2026 figures, also CPI-updated each January). Pass `--domestic` with the right `--domestic-route`, and never quote a distance-band figure for a domestic flight.

The monetary amount is set by distance band (2026 figures): up to 2,000 km, then 2,000 to 4,500 km, then over 4,500 km. Quote the band amount from the reference file and tell the user these amounts are CPI-updated every January so they should confirm the current-year figure. Apply the 50 percent reduction only if the passenger accepted an alternative that arrived within the per-distance window.

**Then add the head most claims leave on the table: exemplary damages (פיצויים לדוגמה) under section 11.** The court may award up to 12,240 NIS per passenger (the 10,000 NIS in the statute, indexed for 2026), with NO proof of harm, where it finds the airline KNOWINGLY failed to give the benefits owed under sections 5, 6, 7, 8, 9(b) or 10. This is often larger than the band amount itself and is a major reason airlines settle, so state it explicitly in the demand letter and in any statement of claim rather than treating the band figure as the whole claim. It is discretionary, so present it as claimed, not guaranteed.

Separately from the money, explain the assistance the airline owed during the wait (food and communication after 2 hours; from 5 to under 8 hours, the passenger's CHOICE of a refund or an alternative flight, and accommodation plus ground transport only where they accepted an alternative departing the next day). Assistance is owed even when an exemption removes the monetary compensation. This ladder applies to DOMESTIC flights too: section 18 applies the whole law to domestic passengers with the necessary changes and carves out only the monetary compensation, which is what the separate regulations set. So a domestic passenger delayed 4 hours is owed the same care, even though their money figure comes from the domestic schedule.

### Step 5: Check exemptions before promising money

Section 6(e) gives the airline exactly THREE grounds, and the burden of proving one is expressly on the carrier, not on the passenger:

1. **Extraordinary circumstances** outside its control that it could not have prevented even doing everything possible. Israeli case law reads this narrowly, so a routine technical fault is usually not an exemption.
2. **A protected strike or lockout** (שביתה או השבתה מוגנות). This is a standalone ground, not a sub-case of the first, so do not argue it as though it were.
3. **Avoiding desecration of Shabbat or a holiday.**

Do not concede a ground just because the airline asserts one, and do not abandon a claim because a strike was involved (an unprotected strike is not a ground). Note the asymmetry on early departures: section 8(b)(1) cross-references only grounds (1) and (2), so a Shabbat-driven early departure still pays.

**The Iron Swords exemption is closed and retroactive, not an open war exemption.** Amendment No. 2 (2025) waived the monetary compensation only for flights whose ticketed date falls in these fixed past windows:

| Window | Effect |
|--------|--------|
| 07.10.2023 to 30.11.2023 | No monetary compensation |
| 01.12.2023 to 29.02.2024 | No monetary compensation only if the airline proves it gave at least 3 days notice |
| 12.04.2024 to 18.04.2024 | No monetary compensation |
| 03.08.2024 to 08.08.2024 | No monetary compensation |
| 01.10.2024 to 05.10.2024 | No monetary compensation |

There is no sunset to expire and no rolling war exemption. **No 2025 or 2026 flight is covered by these windows**, including flights disrupted by the June 2025 Iran exchange. For a flight outside the windows the airline must fall back on the general extraordinary-circumstances defence, which is a much higher bar. Even inside a window, assistance, the refund, and the alternative-flight choice are still fully owed. The exemption also does not apply to judgments already given before the amendment took effect.

**Check for a standing emergency order (Section 9א).** The same amendment added a permanent mechanism: where a declared special situation has been in force more than 14 days, the Minister of Transport may, with Knesset Economy Committee approval, issue an order that reduces accommodation (to no fewer than two nights), changes the alternative-ticket entitlement, shortens the 14-day notice period (to no fewer than 3 days), or negates the monetary compensation entirely. Such an order runs at most 60 days, or 45 days where it negates compensation, and lapses with the emergency declaration. So before applying the default rules to any disruption date, check whether an order was in force for that date rather than assuming the ordinary entitlement.

Separately, while the October 2023 home-front special-situation declaration remains in force, an operator that halted all of its flights to and from Israel must offer an alternative ticket from a different origin or to a different destination, with the passenger's written consent.

### Step 6: Draft the demand letter

Write a short, firm Hebrew letter to the airline that states the flight details, the trigger, the exact amount owed with the legal basis (חוק שירותי תעופה), and a statement that the passenger will file a small claims suit if unpaid. Cite the statutory payment deadlines so the demand has teeth: a fare refund is due within 21 days of a written request, and the First Schedule monetary compensation (cancellation, long delay, early departure) is due within 45 days of a written request. If the disruption caused real extra costs (an unplanned hotel night, a missed connection, replacement tickets), note that these consequential losses are claimed in addition to the statutory amount, with receipts. Keep Hebrew natural and direct. Attach the booking, the boarding pass or check-in proof, and any evidence of the disruption (the airline's cancellation or delay notice, an SMS, or a screenshot of the airport board).

### Step 6.5: Check whether EU261 also applies, and claim in the right order

Israeli law and EU Regulation 261/2004 are separate regimes that OVERLAP, so "this is an Israeli flight, use the Israeli law" is the wrong test. EU261 covers any flight DEPARTING an EU airport regardless of carrier, and a third-country-to-EU flight operated by an EU carrier. So:

| Route | Israeli law | EU261 |
|-------|-------------|-------|
| Paris/Rome/Frankfurt to TLV, any carrier | Yes (arrives Israel) | Yes (departs the EU) |
| TLV to Paris on Air France or Lufthansa | Yes (departs Israel) | Yes (EU carrier into the EU) |
| TLV to Paris on El Al | Yes | No |
| TLV to New York on Delta | Yes | No |

This matters because the thresholds differ sharply. A 4-hour delay on a Paris to TLV flight is worth nothing under the Israeli law (well under the 8-hour cancellation threshold) but 400 EUR under EU261. Telling that passenger "nothing is owed" is wrong.

Two provisions govern the interaction. Section 16 preserves rights under any other law, so merely BEING eligible under EU261 does not extinguish the Israeli claim. Section 20 then says a passenger who has actually RECEIVED a benefit under foreign law loses the Israeli benefit OF THAT SAME TYPE. That is disqualification by benefit type, not a deduction and not a top-up, which makes sequencing irreversible: **work out which regime pays more for this specific disruption and claim that one first.** Claiming the lower regime first can forfeit the higher one. Because it is type-scoped, a passenger paid EU261 money but refused a hotel can still claim the Israeli assistance.

### Step 7: Route the escalation

If the airline refuses or ignores the demand, the realistic next step is a small claims suit (תביעה קטנה). Hand the user off to the israeli-small-claims-court skill for drafting and filing.

Set expectations on the regulator honestly: the Aviation Services Law contains no enforcement chapter and designates no regulator to order payment to a passenger. The Civil Aviation Authority handles licensing, airworthiness and safety, not individual compensation claims, so a complaint there will not get the money paid. The Israeli Consumer Council is useful for guidance and pressure, but it also cannot order payment. Do not send the passenger to a regulator instead of to court.

Two practical points for the filing:
- The small claims ceiling is about 39,900 NIS (2026, CPI-updated),. A family claim that stacks band amounts plus section 11 exemplary damages plus consequential losses can exceed the ceiling, in which case it must be trimmed or filed in the magistrates court instead.
- Suing a foreign airline requires serving its Israeli representative for service of court documents; the Civil Aviation Authority publishes that register, which is the one genuinely useful thing it offers here.

Remind the user that the limitation period is 4 years from the disruption.

## Examples

### Example 1: Long-delayed flight from Europe

User says: "My TLV to Rome flight left 9 hours late. Am I owed anything?"
Actions:
1. Scope: TLV departure, the law applies.
2. Trigger: 9-hour delay is over the 8-hour international threshold, treated as a cancellation.
3. Distance: TLV to Rome is about 2,270 km great-circle, which is OVER the 2,000 km line, so it falls in the second band (2,450 NIS as of 2026). Rome is the classic trap here: it feels like "nearby Europe" but sits just above the boundary, so measure rather than assume.
4. Run `python3 scripts/compensation_calc.py --distance-km 2270 --delay-hours 9`.
Result: Explain the amount, the assistance the airline owed during the wait, and draft the demand letter.

### Example 2: Cancelled flight with last-minute notice

User says: "El Al cancelled our flight to New York 3 days before. Family of four."
Actions:
1. Scope and trigger: cancellation with under 14 days notice, the law applies.
2. Distance: TLV to New York is over 4,500 km, so the top band (3,670 NIS as of 2026), per passenger.
3. Explain the refund-versus-rebooking choice and that each passenger has a separate claim.
Result: Compute the total, explain the choice, draft a single demand letter listing all four passengers.

### Example 3: Old disruption, still claimable

User says: "A flight got cancelled on me about 3 years ago, too late to do anything?"
Actions:
1. Check the date against the 4-year limitation period.
2. If within 4 years, proceed to classify and compute as normal.
Result: Confirm it is still claimable and draft the demand letter.

## Recommended MCP Servers

| MCP | Why | Source |
|---|---|---|
| ben-gurion-flights | Pull real-time and recent Ben Gurion (TLV) arrivals and departures from the Israel Airports Authority feed to evidence that a flight was delayed or cancelled, which strengthens the demand letter and a later small claims filing. | https://www.iaa.gov.il/ |

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Aviation Services Law (full statute, Nevo) | https://www.nevo.co.il/law_html/law00/119611.htm | Distance bands, the 50 percent windows, the 4-year limitation, the scope clause |
| Statutory passenger-rights notice (El Al PDF) | https://www.elal.com/SiteCollectionDocuments/About-ELAL/Passengers-Rights/Aviation-Services-Law-HE-200918.pdf | The 2, 5, and 8-hour assistance ladder, denied boarding, downgrade, early departure |
| Kol Zchut, compensation for a cancelled flight | https://www.kolzchut.org.il/he/פיצוי_במקרה_של_טיסה_שהתבטלה | The 2026 amounts, extraordinary circumstances, the limitation period |
| Civil Aviation Authority of Israel | https://www.gov.il/he/departments/civil_aviation_authority_of_israel | NOT an enforcement route for compensation. Useful only for the register of Israeli representatives for service of court documents on a foreign carrier |
| Israeli Consumer Council, aviation rights | https://www.consumers.org.il/category/aviation-law-benefits | Consumer-side guidance and the complaint route |

## Bundled Resources

### Scripts
- `scripts/compensation_calc.py` -- Computes the entitlement (amount by distance band, the 8/3-hour thresholds, the 50 percent reduction, exemptions). Run: `python3 scripts/compensation_calc.py --example`

### References
- `references/compensation-table.md` -- The full 2026 rate table, assistance ladder, exemptions, and scope. Consult before quoting any figure.
- `references/domain-checklist.md` -- The coverage contract for this skill.

## Gotchas

- Do not use EU261 numbers. The single most common error is quoting 250/400/600 EUR or the EU261 3-hour delay threshold for an Israel flight. Israel's law is NIS-denominated (1,530 / 2,450 / 3,670 as of 2026) with an 8-hour international delay threshold. They are different regimes.
- The amounts change every January. They are CPI-linked and rounded to the nearest 10 NIS. A figure that was right last year may be stale. Always say "as of 2026, confirm the current-year amount."
- Assistance and money are separate. A passenger can be owed food, accommodation, and a refund even when an exemption (or the Iron Swords window) removes the monetary compensation. Do not collapse the two.
- An accepted alternative can halve the money, but only if it arrived within the 2, 3, or 4-hour window for the distance. Outside the window, the full amount stands. Do not apply the 50 percent reduction automatically just because a rebooking happened.
- Do not concede an "extraordinary circumstances" exemption on the airline's say-so. Israeli case law reads it narrowly; a routine technical or crewing fault usually does not qualify.
- Per-passenger, not per-booking. Each passenger on the reservation has their own claim. A family of four is four claims.

## Troubleshooting

### Error: "The user is sure it is 600 euros"
Cause: They are thinking of EU261, not the Israeli law.
Solution: Explain that for a flight to or from Israel the Israeli Aviation Services Law governs, with NIS amounts, so 600 EUR is not the Israeli figure. But do NOT tell them the regimes are mutually exclusive, because often they are not: EU261 also covers any flight departing an EU airport, and a third-country-to-EU flight on an EU carrier, so many Israel routes sit under both. Run the Step 6.5 test. If both apply, work out which pays more for this disruption and claim that one FIRST, because section 20 disqualifies an Israeli benefit only of the same TYPE already received under foreign law. A passenger paid under EU261 but refused a hotel can still claim the Israeli assistance.

### Error: "The airline says it was weather / a technical fault, so nothing is owed"
Cause: The airline is asserting an extraordinary-circumstances exemption.
Solution: Assistance is still owed regardless. For the money, the exemption only holds if the cause was genuinely beyond the airline's control AND it did everything possible. A routine technical fault usually does not qualify. Keep the demand and let the airline prove the exemption.

### Error: "I cannot find the exact flight distance"
Cause: Borderline distance between two bands.
Solution: Use a great-circle distance lookup for the origin-to-final-destination pair. For a connecting itinerary use the whole-journey distance. If still borderline, state both possible amounts and note which band applies at the exact distance.
