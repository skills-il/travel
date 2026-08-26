---
name: israeli-travel-planner
description: Plan domestic travel in Israel with local transportation, accommodations, national parks, and cultural considerations. Use when user asks about traveling in Israel, Israeli hotel chains, bus routes, Israel Railways, Rav-Kav card, national parks, tiyul b'aretz, Dead Sea, Eilat, or trip planning within Israel. Covers Egged/Dan/Kavim buses, train schedules, Rashut HaTeva sites, Shabbat travel restrictions, and seasonal advice.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
---


# Israeli Travel Planner

## Bus Companies
| Company | Coverage |
|---------|----------|
| Egged | Nationwide intercity; part of Jerusalem (see note) |
| Dan | Tel Aviv metro (Gush Dan) |
| Kavim | Central Israel, Modi'in |
| Metropoline | Sharon region |
| Superbus | Jerusalem cluster, Emakim (northern valleys), Gush Dan, Haifa Metronit |
| Nateev Express | Beer Sheva, Negev |
| Electra Afikim (formerly Afikim) | Jordan Valley, Beit She'an, Samaria, central cities |

Jerusalem urban service is not run by a single company: it is tendered in clusters and more than one operator runs city lines. Do not tell a user "take the Egged bus" for an intra-Jerusalem trip without checking the specific line.

## Israel Railways Key Routes
- Tel Aviv - Haifa: ~1 hour, every 20-30 min
- Tel Aviv - Jerusalem: ~32-34 min scheduled on the fast line (the sub-30 figure is non-stop design speed, not a timetable)
- Tel Aviv - Beer Sheva: ~1.5 hours
- Haifa - Nahariya: ~40 min
- Acre - Karmiel: ~25 min (Galilee line, stations Ahihud and Karmiel)
- Haifa - Beit She'an: ~1 hour (Jezreel Valley line; single track, so frequency is low, check before relying on it)

There is no passenger rail to Eilat. The line has been discussed and partly budgeted but is not built; Dimona is the southernmost passenger station. Route Eilat trips by bus or by air, never by train.

## Rav-Kav Card
Rechargeable smart card for all public transport. Types: Personal (with photo) and Anonymous. Load passes: daily, weekly, monthly, or stored value. The Rav-Kav is no longer the only fare medium: a physical Rav-Kav can be loaded remotely through the Rav-Kav Online, HopOn (Rav-Pass) apps and ravkavonline.co.il instead of only at a kiosk or with the driver.

EMV contactless (tap a physical credit card, Apple Pay or Google Pay) is spreading and is not Egged-bus-only: Dan has accepted contactless cards on its central-Israel buses since October 2022, and Egged rolled out a contactless pilot in Eilat, Jerusalem and Haifa in early 2026. EMV acceptance on Israel Railways has been announced across several procurement cycles; confirm on rail.co.il before telling a passenger they can tap at the gates.

## Public Transport Fares
Under the "Derech Shava" (Equal Path) reform, single-ride fares are set by distance travelled rather than by operator. Current single-ride bus fares:
- Up to 15 km (urban): 8 NIS, including 90 minutes of free transfers within the zone.
- Up to 40 km: 14.5 NIS.
- Up to 75 km: 19 NIS.
- Up to 120 km: 19 NIS.
- Up to 225 km: 30.5 NIS.
- Over 225 km: 74 NIS.

A daily cap ("chofshi yomi") is the amount beyond which every further ride that day is free. Bus caps by band: 17.5 NIS up to 15 km, 29 NIS up to 40 km, 37.5 NIS up to 75 km, 37.5 NIS up to 120 km, 60.5 NIS up to 225 km, and 79.5 NIS over 225 km. Every band has a cap, including the longest. A nationwide unlimited monthly bus pass is 315 NIS. Seniors aged 67 and over travel free nationwide.

Two things agents get wrong here. First, "bus" in the official tariff means bus plus light rail (Dankal and Jerusalem), Metronit, Rakavlit and the Carmelit, so a light-rail leg is priced in the bus column, not as a separate mode. Second, Israel Railways has its OWN higher column: a trip including the train uses the "combined rail" fares and caps, not the bus ones. Do not quote a bus figure for a journey that includes a train. Check the live table at https://bus.gov.il/FaresDistance before quoting any number.

Separately from the distance bands, the "Tzedek Tachburti" (Transport Justice) scheme discounts fares by rider profile: 50% for youth aged 5-18, women aged 62-67, holders of a qualifying geographic profile, riders with disabilities and National Insurance benefit recipients; 33% for ages 18-26. Profiles also exist for children up to age four, for soldiers and security forces, and for students.

Two operational points matter more than the percentages. The discount is not automatic: the rider must have the profile registered on their Rav-Kav or app, which is done online or at an "Al HaKav" service centre, and until then they pay full fare. And discounts do not stack, the system applies the single highest one the rider qualifies for. Validation is mandatory on every boarding of a bus or train even for a rider travelling free or holding a monthly pass.

## Shabbat and Chag Travel
State-operated public transit stops Friday afternoon and resumes Saturday night. The same pattern applies to Yom Tov days, which planners routinely forget: both days of Rosh Hashana, the first and last days of Pesach, Shavuot, and the first and last days of Sukkot shut state transit like a Shabbat, with service winding down on the eve as it does on a Friday. Check the traveler's actual dates against the Hebrew calendar before planning any intercity leg. Chol HaMoed Pesach and Sukkot are the opposite problem: transit runs, but these are the busiest domestic-travel weeks of the year, popular INPA sites fill and close their gates to further entry during the morning, and car parks fill first. Book ahead in those weeks at any site that offers coordination. But "no transit on Shabbat" is now wrong as a blanket statement, and telling a traveler to book a taxi they do not need is the most common failure in this domain.

- **Municipal and non-state weekend services exist in parts of the country** and are the reason the blanket claim is wrong. Haifa has long had limited municipal Shabbat bus service, and various free or low-cost weekend services have operated in central-Israel municipalities and in Jerusalem. Coverage is set locally and changes, so treat it as a per-city question: check the specific origin and destination on Moovit or with the local authority before telling a traveler they have no option.
- Always available: private taxis and ride apps, and driving. Sherut (shared taxi) is NOT universal: it runs on a limited set of corridors, so confirm the specific route exists rather than offering it as a general Shabbat fallback.
- Timing matters more than the day: transit stops roughly two to three hours before sundown on a Friday or chag eve and resumes about an hour after sundown. Sundown moves by around three hours across the year, so "Friday afternoon" is unusable in winter. Work from the actual sundown time for the date.
- **Yom Kippur**: intercity transit winds down from midday on erev Yom Kippur, the airport and seaports close, and roads are effectively empty because driving is not socially acceptable. Describe the practical effect rather than making a claim about what the law does or does not require.

## Hotel Chains
- Dan Hotels: luxury chain (city and resort)
- Isrotel: resort and family hotels (strong in Eilat and the Dead Sea)
- Fattal/Leonardo: mid-range city and resort hotels
- Zimmerim: country lodges and cabins in the Galilee and Golan
- Dead Sea range: Ein Bokek hotel strip (full-service resorts) versus the Ein Gedi hostel (budget)

Note: rates swing widely by season, location and event dates. Check current prices on booking sites rather than quoting a fixed figure.

## Top National Parks (Rashut HaTeva)
Masada, Ein Gedi, Banias, Caesarea, Tel Dan, Rosh HaNikra, Timna Park, Ein Avdat.
Single adult entry runs about 31 to 46 NIS at the main tourist sites (Ein Gedi and Banias 31, Masada 37, Caesarea 46), with children roughly half; smaller sites are lower. Tourist multi-site cards: Blue (3 sites) 90 NIS, Green (6 sites) 130 NIS, Orange (unlimited) 175 NIS. Each is valid for two weeks from the first visit. None of them covers the Masada cable car, and none covers the City of David.

INPA's annual subscription (sold as Matmon) is the residents' option rather than a visitor product; for a short trip the tourist cards are the right comparison. The tier prices are NOT on the public price list, which is why they are easy to get wrong: they live on INPA's separate sales portal at fe.sales.parks.org.il. Individual is 208 NIS, with 187 on renewal and 354 for two years; a couple is 316 and a senior is 105. One rule surprises people: a subscription covers entry everywhere EXCEPT the water sites (Chorshat Tal, Achziv, Gan HaShlosha/Sachne, Palmachim, and the sea turtle rescue centre visitor centre), where subscribers still pay 50%.

Before sending anyone to a specific park, check the live alerts banner on parks.org.il. Closures for heat load, flooding, trail damage, safety works and planned power outages are routine and are posted per site, and several Dead Sea and Judean Desert routes carry standing collapse and sinkhole warnings.

Masada cable car: a SEPARATE charge the Blue/Green/Orange tourist cards do NOT cover. Do NOT tell a user the cable car is unavailable at sunrise: INPA runs a dedicated sunrise cable car ("זריחה לכולם") on selected dates through the year, by advance registration. On ordinary days the last cable car up leaves an hour before closing, so check the specific date rather than generalising from the posted gate hours. Official Masada entrance is about 37 NIS adult (21 child, 19 senior); the cable car is billed separately and does NOT include entrance, at about 32 NIS one-way (16 child) or 54 NIS round-trip (32 child). Budget the cable car on top of entrance and any tourist card.

## Driving and Car Rental
Both worked examples below route the traveler into a car, so the skill has to carry the basics rather than disclaim them.
- **Highway 6 is barrier-free electronic tolling.** There are no cash booths; the road is billed to the registered keeper afterwards. On a rental that means the rental company is billed and rebills the driver later, typically adding a per-transaction administration fee on top of the toll. Do not quote the published toll as the traveler's cost, and warn them that a short segment can cost several times the toll once the fee lands. The same applies to the Carmel Tunnels and to Fast Lane use.
- **Rental eligibility trips people up.** Israeli rental companies set a minimum driver age and add a young-driver surcharge below a higher age threshold, require a credit card in the driver's own name for the deposit, and structure collision and theft waivers differently from what European or North American renters expect. Tell the traveler to confirm the age rules, the deposit method and what the waiver actually covers before booking, and do not quote a figure for any of them.
- **Cross-border and area restrictions** are set by each rental agreement rather than by a single national rule; a traveler planning to leave Israel or to drive in particular areas must check their specific contract.
- Parking: blue-and-white kerb is paid (commonly via a parking app rather than a meter, which a visitor may not be able to install easily), red-and-white is no parking.

## Ben Gurion Airport Ground Transport
Most domestic itineraries start or end at TLV, and the skill is incomplete without it.
- **Train** is usually the best option: the airport station sits under Terminal 3 and reaches Tel Aviv Savidor in roughly 15-20 minutes, with onward connections north and south. It does not run on Shabbat.
- **Taxi** ranks are official and metered; ride apps also serve the airport.
- **Bus** service to and from the airport is limited compared with rail; do not assume a direct city bus exists.
- On Shabbat and chagim, rail and most buses do not run, so arriving travelers need a taxi or a pre-booked transfer. Flights still land, so this is a real and frequent trap.

## Regional Highlights
- Dead Sea: Ein Gedi + Masada sunrise + floating. Sinkholes have closed stretches of the northern and central Dead Sea shoreline, including the Ein Gedi public beach, which is a different place from both the nature reserve and the hostel. Only use designated open beaches (the Ein Bokek strip is the main one) and check current closures rather than assuming a beach named on an old map is still accessible.
- Eilat: Coral Beach, Timna, VAT-free shopping. Eilat is a VAT-exempt zone, so eligible goods are sold without the standard 18% VAT. Two cautions before promising anyone a saving: the exemption is applied by the Eilat seller at the point of sale rather than claimed back afterwards like a tourist refund, and it does not extend to every category of goods. Check the Tax Authority's current Eilat rules for what qualifies instead of quoting a blanket 18% saving.
- Galilee/Golan: Banias, Tel Dan, wineries, Tzfat
- Jerusalem: Old City, Yad Vashem, Mahane Yehuda
- Tel Aviv: Beaches, Jaffa, Carmel Market, Neve Tzedek

## Examples

### Example 1: Plan a Weekend Trip to the Dead Sea
User says: "Plan a weekend trip from Tel Aviv to the Dead Sea"
Actions:
1. Transport: Egged line 421 from Tel Aviv Savidor toward the Dead Sea (~2 hours 15 min; priced by distance band under Derech Shava, ~19 NIS for the up-to-120 km band). Check it before building a weekend around it: the line runs by ADVANCE RESERVATION and its published operation is weekdays, so it may not serve the Friday or Saturday legs of a weekend trip at all. A rental car via Route 90 is the safer default for a weekend Dead Sea itinerary
2. Accommodation: Ein Bokek hotel strip (full-service resorts) or the Ein Gedi hostel (budget); check current rates on booking sites
3. Activities: Ein Gedi Nature Reserve (entry ~31 NIS adult) -- do not promise specific trails. INPA posts per-trail restrictions for this reserve, including heat-load cutoffs that close routes or bar entry after a set morning hour, and it may require coordinating a visit slot. Read the reserve's page and the site alerts banner on the day. Masada sunrise hike (entrance ~37 NIS; the cable car is a separate charge, ~32 NIS one-way / ~54 NIS round-trip, and does NOT include entrance). Dead Sea bathing at a designated open beach on the Ein Bokek strip
4. Food: Hotel restaurants, Arad for budget dining (20 min drive)
5. Tips: Bring water shoes and sunscreen SPF 50+; in the Dead Sea itself do not submerge your head or open your eyes, rinse in fresh water immediately after, and keep immersion short. For Masada, "arrive early" is not enough guidance, and the gate hours are NOT the trail hours:
   - The Snake Path opens for ascent about an hour before sunrise, well before the posted 08:00 gate opening. INPA advises arriving about half an hour before the trail opens, because of sunrise crowds and ticket queues. The climb takes about an hour and is graded difficult.
   - There is also a sunrise cable car on selected dates by advance registration, so a sunrise visit does not have to be on foot. Check the date.
   - The Roman ramp from the Arad side is about a half-hour climb, graded moderate.
   - Heat load closes the Snake Path on a sliding scale, decided that morning from the meteorological forecast: moderate heat, last ascent 10:00 and last descent 11:00; heavy heat, 08:00 and 09:00; peak summer, 07:00 and 08:00 with the Roman ramp at 11:00/12:00. Check on the day, not the night before.
   - Otherwise the Snake Path closes for ascent two hours before the site closes and for descent one hour before, park entry closes an hour before posted closing, and the last cable car up leaves an hour before closing. Masada also runs an advance visit-coordination booking that guarantees a slot
Result: Complete itinerary with transport, accommodation, costs, and practical tips

### Example 2: Family Day Trip to the Galilee
User says: "Suggest a day trip for a family with kids in northern Israel"
Actions:
1. Route: Drive to Tiberias area via Route 6 + Route 77
2. Morning: Kfar Kedem biblical experience (verify current rates before visiting)
3. Lunch: Decks restaurant on the Kinneret, or falafel in Tiberias (budget option)
4. Afternoon: Hamat Gader hot springs or Kinneret beach (check current pricing)
5. Evening: Return via Route 6 (current toll rates available on toll road website)
Result: Family-friendly Galilee itinerary with kid activities and budget options

## Bundled Resources

### Scripts
- `scripts/plan_route.py` -- Calculates distances and suggests transport options between Israeli cities. Accepts Hebrew city names as well as English slugs. Run `python scripts/plan_route.py --list` for supported cities, or `python scripts/plan_route.py --from "תל אביב" --to "ירושלים"`. Times are estimates from a flat speed model, not timetables.

### References
- `references/israeli-transport-guide.md` -- Comprehensive guide to Israeli public transport (Egged, Dan, Israel Railways, Rav-Kav), national parks pricing, hotel chains, and regional highlights. Consult when planning detailed itineraries or comparing transport options.

## Recommended MCP Servers

For live transit and travel data, pair this skill with:

| MCP Server | What it provides | Install |
|------------|-----------------|---------|
| **israel-railways** | Real-time Israel Railways schedules, platform numbers, occupancy predictions, and service disruption alerts for 68 stations | [Install](https://agentskills.co.il/en/mcp/israel-railways) |
| **openbus** | Real-time bus arrival data from the Ministry of Transport for all Israeli transit operators | [Install](https://agentskills.co.il/en/mcp/openbus) |
| **routes-israel** | Multi-modal transit routing combining Google Routes, GTFS data, and live arrival times | [Install](https://agentskills.co.il/en/mcp/routes-israel) |
| **ben-gurion-flights** | Real-time flight arrivals and departures at Ben Gurion Airport (TLV) from official data | [Install](https://agentskills.co.il/en/mcp/ben-gurion-flights) |
| **israel-hiking** | Hiking trail search, route planning with elevation profiles, water sources, and points of interest | [Install](https://agentskills.co.il/en/mcp/israel-hiking) |
| **ims-weather** | Weather forecasts and alerts from the Israeli Meteorological Service for trip planning | [Install](https://agentskills.co.il/en/mcp/ims-weather) |

When these MCPs are available, use them for real-time transit schedules and travel data instead of the static reference tables above.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| National Public Transport Authority, distance-band tariff | https://bus.gov.il/FaresDistance | Single-ride fares, daily caps and monthly passes per band; bus column vs combined-rail column |
| National Public Transport Authority, discounts | https://bus.gov.il/ | Tzedek Tachburti eligibility profiles and discount rates |
| INPA price list | https://www.parks.org.il/article/price/ | Per-site entry fees, current year, and the live closure/alerts banner |
| INPA money-saving tickets (English) | https://en.parks.org.il/article/money-saving-tickets/ | Blue/Green/Orange tourist card prices and validity |
| Egged payment methods | https://www.egged.co.il/en/information-for-passengers/rav-kav-and-payment-apps | Rav-Kav loading options and EMV contactless rollout |
| Rav-Kav Online | https://ravkavonline.co.il/en/ | Remote card loading and Derech Shava explainers |

## Gotchas
- State-operated public transport does not run from Friday afternoon to Saturday evening, or on Yom Tov days, in most of the country. Agents make BOTH mistakes here: planning a Saturday or chag itinerary on buses and trains that will not run, and telling a traveler in a city that does have weekend service that they are stranded. Treat it as a per-city, per-date question and check the specific origin, destination and date rather than applying a national rule.
- Israeli bus numbers and route names use Hebrew characters. Agents may not recognize that route 17-aleph is a different route from 17. Always include the Hebrew letter suffix.
- A physical Rav-Kav card cannot be loaded via a public API, but since early 2026 it is no longer the only option: the Rav-Kav Online / HopOn / Rav-Pass apps load a Rav-Kav remotely, and EMV contactless (tapping a credit card, Apple Pay or Google Pay at the validator) lets a traveler ride with no Rav-Kav at all. Don't tell users they must visit a physical kiosk or pay the driver.
- Google Maps transit directions in Israel are often inaccurate for bus arrival times. The official source is the Moovit app or the Ministry of Transport GTFS feed. Agents should not rely solely on Google Maps.

## Troubleshooting

### Error: "Bus route information may be outdated"
Cause: Israeli bus routes and schedules change frequently, especially after Egged/Dan restructuring
Solution: Always note that schedules should be verified on Moovit or the bus company website. Provide the Moovit/Google Maps link for real-time data.

### Error: "National park is closed on requested date"
Cause: Parks may close for holidays, weather, or security
Solution: Check the Israel Nature and Parks Authority website (parks.org.il) for closures. Note that parks close early on Fridays and eves of holidays. Suggest alternative nearby attractions.