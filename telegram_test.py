import asyncio

from telethon import TelegramClient, errors
from telethon.tl.functions.help import GetConfigRequest


async def main():
    # These placeholders permit an unauthenticated connectivity check only.
    client = TelegramClient(
        None, 1, "0" * 32, connection_retries=0, request_retries=0,
        auto_reconnect=False,
    )
    try:
        async with asyncio.timeout(20):
            await client.connect()
            await client(GetConfigRequest())
    except (OSError, errors.RPCError) as error:
        print(f"TELEGRAM TEST FAILED ({type(error).__name__})")
    else:
        print("TELEGRAM CONNECTION OK")
    finally:
        await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
