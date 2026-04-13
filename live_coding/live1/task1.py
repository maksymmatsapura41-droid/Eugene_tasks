import asyncio
import random

async def fetch(i):
    await asyncio.sleep(random.random())
    print(f"Fetched {i}")

async def main():
    tasks = [ asyncio.create_task(fetch(i)) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())


