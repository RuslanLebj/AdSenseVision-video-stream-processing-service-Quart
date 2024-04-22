from quart import Quart, websocket
import aiohttp
import cv2
import asyncio
import json
import logging

# Настройки логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Quart(__name__)


def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config


config = load_config()
API_URL = config['api_url']


async def fetch_camera_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            cameras = await response.json()
            return cameras


@app.before_serving
async def load_cameras_and_process():
    cameras = await fetch_camera_data()
    logger.info(f"Fetched cameras data:\n{cameras}")



if __name__ == '__main__':
    app.run()
