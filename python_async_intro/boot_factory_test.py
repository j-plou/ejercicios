import asyncio
import random

BOOTS = 0
CHECKED_BOOTS = 0
SECONDS = 0


async def increase_seconds():
    global SECONDS
    await asyncio.sleep(1)
    SECONDS += 1
    print("Seconds:", SECONDS, "Boots:", BOOTS)


async def clock_seconds():
    while 1:
        await increase_seconds()


async def qa_check_boot():
    global CHECKED_BOOTS
    while 1:
        if CHECKED_BOOTS < BOOTS:
            checking_time = random.choice([5, 10])
            await asyncio.sleep(checking_time)
            CHECKED_BOOTS += 1
            print("Checked boots", CHECKED_BOOTS)
        else:
            print("** NO BOOTS, Coffee time! **", CHECKED_BOOTS)
            await asyncio.sleep(20)


async def make_boot():
    global BOOTS
    manufacturing_time = random.choice([1, 3, 5])
    await asyncio.sleep(manufacturing_time)
    BOOTS += 1
    print("Boots:", BOOTS, "after", manufacturing_time)


async def worker():
    while 1:
        await make_boot()


async def main():
    await asyncio.gather(worker(), worker(), worker(), qa_check_boot(), qa_check_boot(), qa_check_boot(), qa_check_boot(), qa_check_boot(), qa_check_boot(), qa_check_boot(), qa_check_boot(), qa_check_boot(), qa_check_boot(), clock_seconds())


asyncio.run(main())
