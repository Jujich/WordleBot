from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
import os

load_dotenv("config.env")

bot = Bot(token=os.environ.get("WORDLEBOT_TOKEN"), default=DefaultBotProperties(parse_mode='HTML'))
