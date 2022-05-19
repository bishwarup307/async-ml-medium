import asyncio
import time

import aiohttp


async def send_request(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            r = await response.text()
            return r
    return None


async def send_bulk_request(url: str, n: int):
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, url) for _ in range(n)]
        results = await asyncio.gather(*tasks)

    return results


if __name__ == "__main__":
    start = time.perf_counter()
    url = "http://localhost:9009/predict"
    results = asyncio.run(send_bulk_request(url, 8))
    print(f"elapsed: {(time.perf_counter() - start):.2f}")
    print(results)
