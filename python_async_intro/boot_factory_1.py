import asyncio
import random
import datetime

BOOTS = 0
SECONDS = 0
INIT_TIME = 0


async def increase_seconds():
    global SECONDS
    global INIT_TIME
    INIT_TIME = datetime.datetime.now()

    await asyncio.sleep(1)
    SECONDS += (datetime.datetime.now() - INIT_TIME).total_seconds()

    print("Seconds: %.4f - Boots: {}".format(BOOTS) % SECONDS)


async def clock_seconds():
    while 1:
        await increase_seconds()


async def make_boot():
    global BOOTS
    manufacturing_time = random.choice([1, 3, 5])
    await asyncio.sleep(manufacturing_time)
    BOOTS += 1


async def worker():
    while 1:
        await make_boot()


async def main():
    await asyncio.gather(worker(), clock_seconds())


asyncio.run(main())
