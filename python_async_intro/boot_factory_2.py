import argparse
import asyncio
import random


BOOTS = 0
SECONDS = 0


async def increase_seconds():
    global SECONDS
    await asyncio.sleep(1)
    SECONDS += 1
    print("Seconds: {} - Boots: {}".format(SECONDS, BOOTS))


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
    parser = argparse.ArgumentParser()
    parser.add_argument("workers", help="num of workers")
    args = parser.parse_args()
    total_workers = int(args.workers)

    callbacks = [clock_seconds()]
    for i in range(0, total_workers):
        callbacks.append(worker())

    await asyncio.gather(*callbacks)

asyncio.run(main())
