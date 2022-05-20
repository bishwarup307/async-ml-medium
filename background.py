import asyncio

from download_many import COLORS, timer


async def some_background_task(color):
    print(f"starting background task {color}")
    await asyncio.sleep(10)  # <- i am updaloading to s3 in this line
    print(f"finished background task {color}")


async def download_image_async_with_background_task(color: str):
    print(f"downloding {color} image")
    await asyncio.sleep(1)  # i have the image
    print("finished detection model")
    print("finised segmentor model")
    asyncio.create_task(some_background_task(color))
    print(f"finished downloding {color} image")  # i throw the result to customer


async def download_many_async(colors):
    tasks = []
    for color in colors:
        tasks.append(download_image_async_with_background_task(color))

    tasks = asyncio.gather(*tasks)
    _ = await tasks


@timer
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_many_async(COLORS))

    pending = asyncio.all_tasks(loop)
    loop.run_until_complete(asyncio.gather(*pending))


if __name__ == "__main__":
    main()
