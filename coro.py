import asyncio


async def preprocess():
    print("1. Inside preprocess...")
    await asyncio.sleep(1)  # <- suspend and give the control back to the event loop
    print("2. Inside preprocess again...") # <- during when helper is waiting, preprocess resumes again
    print("done preprocessing...") # <- preprocess is finished
    return 


async def helper():  # <- when preprocess is suspended, the event loop starts the helper
    print("inside helper now...")
    await asyncio.sleep(2)  # <- suspend helper and hand over the control to event loop
    print("done helper...") # <- one the wait is over, helper is the only task in the even loop
    return


async def main():
    _ = await asyncio.gather(preprocess(), helper())


if __name__ == "__main__":
    asyncio.run(main())
