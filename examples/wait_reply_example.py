#!/usr/bin/env python3
"""Example: send a message and wait for a text reply (requires configured bot)."""
import asyncio

import telegram_send


async def main() -> None:
    sent_ids = await telegram_send.send(messages=["Reply with any text"])
    try:
        text = await telegram_send.wait_for_reply(
            sent_message_ids=sent_ids,
            wait_timeout=120,
        )
    except telegram_send.WaitReplyTimeout:
        print("No reply in time", file=__import__("sys").stderr)
        raise SystemExit(2) from None
    print(text)


if __name__ == "__main__":
    asyncio.run(main())
