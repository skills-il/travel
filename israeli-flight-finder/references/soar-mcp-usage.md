# Soar Flight Booking MCP (now Rift): usage rules

Endpoint: `https://mcp.rift.co`. Soar rebranded as Rift in 2026: flysoar.ai now redirects to rift.co, the documented endpoint is `https://mcp.rift.co` (the old `mcp.flysoar.ai/mcp` address still answered on 2026-10-25), the server identifies itself as "Rift Flight Booking MCP", and the `soar_*` tool names are unchanged. Search works anonymously (no API key, no sign-in).

## What it is

A US flight search and booking service. Its terms state it is not an airline or charter operator, but that it **does act as the agent that books, pays for and services** a reservation made through it, so refund and dispute support runs through Rift rather than the airline. The terms are governed by Delaware law with binding JAMS arbitration seated in Wilmington, Delaware, and they appoint Rift, with a limited power of attorney, to cancel and rebook a buyer's ticket when the fare drops.

## Tools

| Tool | Use it? |
|------|---------|
| `soar_search_flights` | Yes, read-only price search |
| `soar_book_flight` | **Never.** Flagged destructive; runs sign-in, verification, and payment within one tool |
| Any other tool that appears | No. The server declares that its tool list can change, so do not call anything beyond the search tool |

## Parameters

`origin`, `destination` (city name, metro, airport name, or IATA), `date` (`YYYY-MM-DD`), `return_date` for round trips, `passengers`, or `passengers_detail` (type `adult` / `child` / `infant_without_seat`, with age or birth date) for a family, `cabin`, `stops`, `max_price`, `min_checked_bags`.

## Binding constraints

1. **USD only.** `currency: "ILS"` is rejected with `currency_usd_only`. Never convert with a remembered exchange rate; read a live rate (e.g. Bank of Israel representative rates) or leave the row in USD.
2. **Add the foreign-currency fee.** Israeli card issuers charge roughly 3% on foreign-currency purchases (some cards are exempt). It belongs inside the ranked total, not the notes.
3. **Single inventory pool.** One reseller is not the whole TLV market. Do not assume it surfaces airline site-only promotions or Israeli charter seats. Carrier coverage varies by route and date, so read the carriers off the response rather than assuming any airline is present.
4. **Rate limit.** 5 calls per minute, 30 per hour, per source IP. Unusable for flexible-month or "anywhere cheap" discovery.
5. **Baggage.** Each offer carries its fare brand and carry-on/checked-bag counts. Prefer those over the static airline tables for a Soar-sourced row, or you will charge for a bag already included.
6. **Never a booking venue.** Do not call the booking tool and do not send the traveler to Soar/Rift to buy. Refunds and disputes would run through a US company under Delaware law and Delaware arbitration, the buyer authorizes it to cancel and rebook the ticket on its own initiative, and the Israeli consumer-protection cancellation rules that apply to a seller operating in Israel may not be enforceable against it. Separately, Israeli law gives passengers rights when a flight to or from Israel is cancelled or delayed; route those questions to `israeli-flight-compensation`.
7. **Privacy.** The call sends the traveler's route, dates, and passenger count to a third party. Do not send passport or payment details.
