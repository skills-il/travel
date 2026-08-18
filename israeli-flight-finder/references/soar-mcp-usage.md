# Soar Flight Booking MCP: usage rules

Endpoint: `https://mcp.flysoar.ai/mcp`. Search works anonymously (no API key, no sign-in).

## What it is

A third-party reseller that surfaces flight inventory sourced from Duffel. Its terms state it is **not an airline, charter operator, or travel agency of record**. Its published terms do not name the entity that bills the traveler's card.

## Tools

| Tool | Use it? |
|------|---------|
| `soar_search_flights` | Yes, read-only price search |
| `soar_book_flight` | **Never.** Flagged destructive; runs sign-in, verification, and payment in one call |
| `soar_discover_tools`, `soar_run_advanced_action_tool` | No. Its own docs describe these as loading further tools on demand, so the action surface is not knowable in advance |

## Parameters

`origin`, `destination` (city name, metro, airport name, or IATA), `date` (`YYYY-MM-DD`), `return_date` for round trips, `passengers`, `cabin`.

## Binding constraints

1. **USD only.** `currency: "ILS"` is rejected with `currency_usd_only`. Never convert with a remembered exchange rate; read a live rate (e.g. Bank of Israel representative rates) or leave the row in USD.
2. **Add the foreign-currency fee.** Israeli card issuers charge roughly 3% on foreign-currency purchases (some cards are exempt). It belongs inside the ranked total, not the notes.
3. **Single inventory pool.** One reseller drawing on one aggregator is not the whole TLV market. Do not assume it surfaces airline site-only promotions or Israeli charter seats, which are often the cheapest leisure options from TLV. Carrier coverage varies by route and date, so read the carriers off the response rather than assuming any airline is present.
4. **Rate limit.** 5 calls per minute, 30 per hour, per source IP. Unusable for flexible-month or "anywhere cheap" discovery.
5. **Baggage.** Each offer carries its fare brand and carry-on/checked-bag counts. Prefer those over the static airline tables for a Soar-sourced row, or you will charge for a bag already included.
6. **Never a booking venue.** Do not call the booking tool and do not send the traveler to Soar to buy. With no billing entity named in its terms, the traveler has no clear counterparty for a refund or a disputed charge, and the Israeli consumer-protection cancellation rules that apply to a seller operating in Israel may not be enforceable against a foreign one. Note separately that compensation for a cancelled or delayed flight departing Israel runs against the operating airline under the Aviation Services Law, whoever sold the ticket.
7. **Privacy.** The call sends the traveler's route, dates, and passenger count to a third party. Do not send passport or payment details.
