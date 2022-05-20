import asyncio
import time
from functools import wraps

from serial import download_image, download_image_async

COLORS = ["blue", "red", "green", "yellow"]


def timer(fn):
    """decorator func to measure the execution time of another function"""

    @wraps(fn)
    def wrapper(*args, **kwargs):
        tick = time.perf_counter()
        _ = fn(*args, **kwargs)
        tock = time.perf_counter()
        print(f"time elapsed: {tock - tick: .2f}")

    return wrapper


def download_many(colors):
    """mocks downloading many images serially e.g., with requests"""
    for color in colors:
        download_image(color)


async def download_many_async(colors):
    """mocks downloading many images asynchronously e.g., with aiohttp"""

    await download_image_async("blue")
    await download_image_async("green")
    await download_image_async("yellow")
    await download_image_async("red")


@timer
def main():
    download_many(COLORS)


@timer
def main_async():
    asyncio.run(download_many_async(COLORS))


if __name__ == "__main__":
    main_async()
