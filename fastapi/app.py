import asyncio
import os
import time

from loguru import logger

from fastapi import FastAPI
from fastapi.concurrency import run_in_threadpool

app = FastAPI()


@app.get("/predict")
async def root():
    pid = os.getpid()
    logger.info(f"{pid}:REQUEST RECEIVED")
    await asyncio.sleep(3)  # run export_ortho using aiohttp
    await run_in_threadpool(time.sleep, 2)  # could be running the onnx model
    return {"message": "Hello World"}
