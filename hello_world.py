import asyncio
import time

async def say_after(delay, what):
    print(f"started {time.strftime('%X')}")
    await asyncio.sleep(delay)
    print(what)
    print(f"ended {time.strftime('%X')}")

async def main():
    await say_after(1, 'hello')
    await say_after(2, 'world')

asyncio.run(main())
