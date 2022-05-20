import asyncio
import concurrent.futures
import io
import time
from multiprocessing import Pool

import aiohttp
import requests
from numpy.typing import NDArray
from PIL import Image

unsplash_search_url = "https://source.unsplash.com/random/300x300"


def download_random_image(num: int = 1) -> NDArray:
    """downloads an image using requests"""
    response = requests.get(unsplash_search_url)
    if response.status_code == 200:
        img = Image.open(io.BytesIO(response.content))

    print(f"image {num} shape: {img.size}")


def download_random_images(n: int = 10):
    for i in range(n):
        download_random_image(i + 1)


def download_multithreading(n: int = 10, n_threads: int = 4):
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
        for i in range(n):
            executor.submit(download_random_image, i + 1)


def download_multiprocessing(n: int = 10, n_processes: int = 4):
    p = Pool(n_processes)
    p.map(download_random_image, range(n))


async def download_image_async(session: aiohttp.ClientSession, num: int = 1):
    async with session.get(unsplash_search_url) as response:
        if response.status == 200:
            image_buffer = await response.read()
            img = Image.open(io.BytesIO(image_buffer))
            print(f"image {num} shape: {img.size}")


async def download_images_async(n: int = 10):
    async with aiohttp.ClientSession() as session:
        tasks = [download_image_async(session, i + 1) for i in range(n)]
        _ = await asyncio.gather(*tasks)
    return


if __name__ == "__main__":
    tick = time.perf_counter()
    download_multiprocessing()
    # download_random_images()
    # download_multithreading(n_threads=6)
    # asyncio.run(download_images_async())
    tock = time.perf_counter()
    print(f"elapsed: {tock-tick:.2f} seconds")
