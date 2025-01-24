from db.classes import Daily
from db.engine import engine
from db.db_requests import get_daily_words, reset_daily
from sqlalchemy.orm import Session
from random import choice
from game.play.words_ru import words as words_ru
from datetime import datetime
import asyncio


async def get_daily_word() -> None:
    session = Session(engine)
    with open("game/play/words_en.txt", "r") as f:
        words_en = f.read().splitlines()
    word_en = choice(words_en)
    word_ru = choice(words_ru)
    daily = Daily(
        date=str(datetime.now().date()),
        word_en=word_en,
        word_ru=word_ru
    )
    session.add(daily)
    session.commit()
    session.close()


async def run_daily_cycle() -> None:
    if not await get_daily_words():
        await get_daily_word()
        await reset_daily()
    while True:
        if datetime.now().hour == 0 and datetime.now().minute == 0:
            await get_daily_word()
            await reset_daily()
            await asyncio.sleep(60)
        await asyncio.sleep(1)
