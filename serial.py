import asyncio
import time


def download_image(color: str):
    """mocks downloading an image e.g., with requests"""

    print(f"downloding {color} image")
    time.sleep(1)
    print(f"finished downloding {color} image")


async def download_image_async(color: str):
    """mocks downloading an image asynchronously, e.g., with aiohttp"""

    print(f"downloding {color} image")
    await asyncio.sleep(1)  # <- download happening here
    print(f"finished detection model")
    print(f"finished downloding {color} image")


def main():
    download_image(color="red")


def main_async():
    asyncio.run(download_image_async("blue"))


if __name__ == "__main__":
    main_async()
