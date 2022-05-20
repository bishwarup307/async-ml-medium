import asyncio

from download_many import COLORS, timer
from serial import download_image_async


async def download_many_async_gather(colors):
    """magic is finally happening"""
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
