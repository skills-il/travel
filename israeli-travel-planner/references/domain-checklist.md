# Domain Checklist: Israeli Travel Planner (public transport + national parks)

Scope: domestic travel in Israel relying on public transport and national parks, for a 2026 trip. Used to review the skill for current, correct fare / ticketing / park-fee / closure guidance. Every figure below is backed by a row in evidence.json.

## Must cover (a traveler is misled without these)

- **Current single-ride fare and the 90-minute transfer.** Post-25-April-2025 Derech Shava: 8 NIS for a ride up to 15 km, including 90 minutes of unlimited free transfers in the yellow zone. Source: https://bus.gov.il/FaresDistance
- **Current single-ride distance-band prices (bus column, effective 25.04.2025).** up to 15 km = 8 ; up to 40 km = 14.5 ; up to 75 km = 19 ; up to 120 km = 19 ; up to 225 km = 30.5 ; over 225 km = 74 NIS. Source: https://bus.gov.il/FaresDistance
- **Daily caps by band (bus column).** up to 15 km = 17.5 ; up to 40 km = 29 ; up to 75 km = 37.5 ; up to 120 km = 37.5 ; up to 225 km = 60.5 ; over 225 km = 79.5 NIS. EVERY band has a cap. Source: https://bus.gov.il/FaresDistance
- **Do not read across columns.** The official table has separate bus and combined-rail columns for single ride, daily cap and monthly. Cycles up to v1.3.0 published the TRAIN single-ride column as if it were the bus daily caps, understating every cap materially. Always confirm which column a figure came from. Source: https://bus.gov.il/FaresDistance
- **Rider-profile discounts (Tzedek Tachburti).** 50% for ages 5-18, women 62-67, qualifying geographic profiles, riders with disabilities and National Insurance benefit recipients; 33% for ages 18-26. The discount requires the profile to be registered on the Rav-Kav or app first. No stacking (highest applies automatically); validation mandatory on every boarding. Source: https://bus.gov.il/Discounts
- **Nationwide unlimited monthly (Chofshi Artzi).** ~315 NIS for bus + light rail (up to 225 km). Source: https://ravkavonline.co.il/en/derekh-shava
- **Senior free-travel age.** 67+ ride free nationwide (lowered from 75, effective 25.04.2025). Source: https://ravkavonline.co.il/en/derekh-shava
- **Payment medium shift (Rav-Kav to app/EMV).** Rav-Kav still works; physical Rav-Kav can be loaded remotely via Rav-Kav Online / HopOn (Rav-Pass) apps + ravkavonline.co.il; EMV contactless (physical credit card, Apple Pay, Google Pay at the validator) is spreading but not universal. Source: https://www.egged.co.il/en/information-for-passengers/rav-kav-and-payment-apps
- **EMV is not Egged-only.** Dan accepts contactless on central-Israel buses since October 2022 and Egged ran an early-2026 pilot in Eilat, Jerusalem and Haifa. Source: https://en.wikivoyage.org/wiki/Public_transit_in_Israel
- **National-park entry fees AND the Masada cable-car surcharge.** Single adult entry runs 31 to 46 NIS at main tourist sites (Ein Gedi 31, Banias 31, Masada 37, Caesarea 46, Coral Beach 40). The Masada cable car is a separate charge the multi-site cards do NOT cover, and both cable-car fares are published explicitly as excluding entry. Source: https://www.parks.org.il/article/price/ ; https://www.parks.org.il/reserve-park/%D7%92%D7%9F-%D7%9C%D7%90%D7%95%D7%9E%D7%99-%D7%9E%D7%A6%D7%93%D7%94/
- **Park multi-site tourist cards.** Blue (3 sites / 2 weeks) 90 NIS, Green (6 sites / 2 weeks) 130 NIS, Orange (unlimited / 2 weeks) 175 NIS; tourists only, exclude the Masada cable car. Source: https://en.parks.org.il/article/money-saving-tickets/
- **Park early closing on Fridays / holiday eves.** Parks close earlier on Fri and holiday eves; verify closures at parks.org.il. Source: https://www.parks.org.il/article/price/

## Should cover

- **Matmon annual subscription** (residents' alternative to tourist cards): INPA does not publish tier prices on its public price list, so state no figure and route the user to parks.org.il. What IS published: subscribers pay nothing except at the water sites (Chorshat Tal, Achziv, Gan HaShlosha/Sachne, Palmachim, sea turtle rescue visitor centre), where they pay 50%. Source: https://www.parks.org.il/article/price/
- **Live park closures.** Per-site closures for heat load, flooding, trail damage and safety works are routine and are posted on the INPA alerts banner; several Dead Sea and Judean Desert routes carry standing collapse and sinkhole warnings. Ein Gedi is advance-booking only. Source: https://www.parks.org.il/article/price/
- **Weekend transit is not uniformly absent.** Municipal and non-state weekend services operate in parts of the country. Treat "no transit on Shabbat" as a per-city question to check on Moovit or with the local authority, not a national fact, and do not publish a municipality list without a live source. (structural: how to reason, not a rate)
- **Yom Kippur.** Describe the practical effect (intercity transit stops from midday on erev, airport and seaports close, roads effectively empty) rather than asserting what the law does or does not require. (structural)
- **No passenger rail to Eilat.** Source: https://en.wikivoyage.org/wiki/Public_transit_in_Israel
- **Jerusalem urban bus service is tendered in clusters to more than one operator**, so it is not a single-company network. Check the specific line; do not name operators without a live source. (structural)
- **Israel Railways contactless: UNVERIFIED.** Rail EMV acceptance has been announced across several procurement cycles, but the only source previously cited here was a 2018 tender announcement written in the future tense, which cannot evidence a live capability. Do not assert it; tell the user to confirm on rail.co.il. Re-check next cycle.
- **Galilee / peripheral rail lines.** Acre-Karmiel (2017) and Jezreel Valley Haifa-Beit She'an (2016) lines. Source: https://en.wikipedia.org/wiki/Railway_to_Karmiel
- **Live-data caveat.** Google Maps transit times unreliable in Israel; use Moovit / MoT GTFS. Source: operational knowledge.
- **Hebrew route-letter suffix** (17-aleph is not 17). Source: operational knowledge.
- **Bus operator list incl. rebrands** (Electra-Afikim, Superbus, Nateev Express, Metropoline). Source: https://en.wikipedia.org/wiki/Electra-Afikim
- **Eilat VAT-free zone** (saving the standard 18% VAT on eligible goods). Source: https://sovos.com/regulatory-updates/vat/israel-vat-rate-increase-to-18-from-january-1-2025/
- **Reserved/booking-only intercity lines** (e.g. 421 to the Dead Sea runs limited times, ~133 min, booking advised). Source: Moovit line 421 route page (see deadsea-421-fare-band in evidence.json).

## Out of scope

- International flights / outbound travel (skill is domestic; ben-gurion-flights MCP handles arrivals/departures separately)
- Car-rental contracts, insurance, fuel-card mechanics (gas price ceiling is a context note only)
- Hotel booking transactions and real-time room pricing (skill gives qualitative tiers only)
- Real-time schedules / live arrivals (delegated to MCP servers: openbus, israel-railways, routes-israel)
- Hiking trail navigation specifics (delegated to israel-hiking MCP)

## Authoritative sources

- Rav-Kav Online (fares, reform, remote loading): https://ravkavonline.co.il/en/derekh-shava
- National Public Transport Authority, fare tables: https://bus.gov.il/FaresDistance (the former pti.org.il/DerekhShava/ URL now redirects here and serves an empty SPA shell to non-browser fetchers)
- Egged payment methods: https://www.egged.co.il/en/information-for-passengers/rav-kav-and-payment-apps
- Israel Nature and Parks Authority price list: https://www.parks.org.il/article/price/
- Israel Nature and Parks Authority money-saving tickets: https://en.parks.org.il/article/money-saving-tickets/
- Masada National Park (entry + cable car): https://en.parks.org.il/reserve-park/masada-national-park/
