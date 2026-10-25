# Flight Comparison Workflow Script

Reference workflow for an AI agent helping a user compare flights from Israel. The goal is a REAL comparison with live fares, not a list of websites. If live fares cannot be read, the agent hands over pre-filled search links instead of inventing numbers.

## Input Parameters

- **Origin**: Ben Gurion Airport (TLV) by default
- **Destination**: Specific city / airport code, or "anywhere / cheapest"
- **Dates**: Specific dates, or flexible ("cheapest month")
- **Passengers**: Adults, each child's age on the travel dates, lap infants under 2, and which passport each traveler will use
- **Observance**: Does anyone keep Shabbat or Yom Tov?
- **Baggage needs**: Carry-on only, or how many checked bags in total
- **Preferences**: Nonstop only, specific airline, budget ceiling

## Comparison Workflow

### Step 1: Gather Requirements
Assume TLV as origin; ask only for what is missing:
1. Where to (or "anywhere cheap")?
2. When (specific dates or a flexible month)?
3. Who is flying: adults, each child's age, lap infants, and which passport each will use?
4. How many checked bags in total, or carry-on only?
5. Nonstop only, or connections OK?
6. Does anyone keep Shabbat or Yom Tov?
7. Airline preference or budget ceiling?

### Step 2: Build Pre-Filled Search Links
Substitute the destination and dates into the verified templates (see `references/comparison-platforms.md`):
- Google Flights: `https://www.google.com/travel/flights?q=Flights+from+TLV+to+{CITY}+on+{YYYY-MM-DD}+returning+{YYYY-MM-DD}&curr=ILS&gl=IL&hl=he`
- Skyscanner: `https://www.skyscanner.co.il/transport/flights/tlv/{dest}/{YYMMDD}/{YYMMDD}/` (lowercase airport code, e.g. `ath`; for a whole month or "Everywhere", use the search-form options)
- KAYAK: `https://il.kayak.com/flights/TLV-{DEST}/{YYYY-MM-DD}/{YYYY-MM-DD}?sort=price_a`
- Every link opens for 1 adult. Set the real passenger mix on each platform's search form before reading prices; do not guess passenger query parameters.

### Step 3: Pull the Live Fares
Open each link and read the top 3-5 results: airline, fare brand, price in shekels, whether that price is per person or for all passengers, stops, total duration, times.
- Use a real browser tool (or flights MCP) for Google Flights and Skyscanner. All three platforms, KAYAK included, render fares with JavaScript, so a plain `WebFetch` returns an empty shell with no prices.
- If no browser tool is available and the Rift (formerly Soar) MCP (`https://mcp.rift.co`) is connected, call `soar_search_flights` (`origin`, `destination`, `date`, `return_date`, `passengers`) for structured live fares. Binding rules: it prices in USD only; never convert with a remembered exchange rate; add the ~3% Israeli card conversion fee into the ranked total; prefer the offer's own baggage counts over the static tables; treat it as a single source and say so; never call `soar_book_flight` and never send the traveler to Soar to buy. Anonymous limit 5/min, 30/hr per IP, so it cannot serve flexible-month searches.
- Cross-check at least two platforms; the same route can differ noticeably between them.

### Step 4: Calculate Total Cost
Rank on the booking total for the whole party: total = fare for the whole itinerary + paid extras (carry-on, checked bags beyond the fare's allowance, seats), each per passenger and per direction.
- Fare: if the platform shows the price for all passengers, use it once; if per person, add each passenger's own fare. Count a round-trip fare once.
- Carry-on is paid on Israir outside New York ($30 per direction) and Wizz (Priority), included on El Al; add it even for carry-on-only trips. Do not add carry-ons or bags the fare already includes. Seats only for passengers who occupy one (not lap infants). Use advance online prices and say so.
- Bag fees are per passenger, per bag, per direction: four Israir first bags at $65 round trip are 4 x $65 x 2 = $520.
- Families need adjacent seats: on basic fares add a seat fee for every seated passenger and direction.
- Carriers without a table in the skill (Arkia, Wizz, Aegean, the El Al Lite bag add-on): read the bag and seat price for that fare brand in the carrier's own booking flow.
- Add the ~3% Israeli card foreign-currency fee only to amounts the card is charged in foreign currency. The Israir baggage table and any Rift fare are in USD while the comparison table is in NIS: convert with a rate you read this session and state it; never convert from memory.
- El Al includes a bag on Classic and up, while Israir (outside New York) and Wizz charge for almost everything, so a low base fare often loses once a 23 kg bag is added. Read Arkia's fees live in its booking flow. Aggregators usually show El Al's Lite fare, so check the Classic price on elal.com before concluding.

### Step 4.5: Check Feasibility
Before ranking, drop or flag any option that fails: entry documents for every passenger and the passport they will use, including transit countries (see the skill's Entry Requirements section); for observant travelers, every flight must land before candle-lighting with a margin of several hours (hebcal.com) and not depart before nightfall; El Al does not fly on Shabbat or Jewish holidays. Put the reason in the Notes column.

### Step 5: Present Comparison
Format the REAL fares, cheapest total first:

| Option | Airline | Route / Stops | Base (NIS) | Extras (NIS) | Total (NIS) | Source | Notes |
|--------|---------|---------------|-----------|-----------|------------|--------|-------|
| 1 | ... | ... | ... | ... | ... | ... | ... |

### Step 6: Recommend
- Cheapest overall (including extras)
- Best value (price vs. stops and timing)
- Best for families (most generous baggage)
Include the Step 2 links so the user can book or re-check the live price.

## Never Invent a Price
Every number in the table, including any exchange rate used to convert a USD or EUR figure into shekels, must come from a page loaded this session. If live prices cannot be read (no web/browser access, bot-block, or captcha), do NOT write numbers -- hand over the pre-filled Step 2 links and say plainly they open live results, because you could not read the fares this turn. A fabricated comparison is worse than none.

## Seasonal Advice
- Jewish holidays (including Hanukkah) and Christmas/New Year: warn that prices climb in the weeks before the holiday, suggest booking several weeks ahead, and book now if the holiday is already close. Take holiday dates from hebcal.com, not memory.
- Flexible on dates: use the Skyscanner whole-month view or Google Flights date grid to find the cheapest window (January and the shoulder seasons are usually quieter).
- Tight budget: check Wizz Air for European routes, but warn that add-on costs (bags, seats) erode the low base fare.
