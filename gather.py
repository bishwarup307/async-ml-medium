import asyncio

from serial import download_image_async
from download_many import COLORS, timer


async def download_many_async_gather(colors):
    tasks = []
    for color in colors:
        tasks.append(download_image_async(color))

    tasks = asyncio.gather(*tasks)
    _ = await tasks


@timer
def main():
    asyncio.run(download_many_async_gather(COLORS))


if __name__ == "__main__":
    main()
