from db.classes import User, Settings, Daily
from db.engine import engine
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import select

available_lang = ["en", "ru"]


async def insert_user(user_id: int, username: str) -> bool:
    session = Session(engine)
    try:
        user = User(
            tgId=user_id,
            username=username,
        )
        settings = Settings(
            tgUserId=user_id,
        )
        session.add(user)
        session.add(settings)
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False


async def get_user_stats(user_id: int) -> dict | None:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        session.close()
        return {
            "win": user.win,
            "lose": user.lose,
            "dwin": user.dwin,
            "dlose": user.dlose,
            "streak": user.streak,
            "longest_streak": user.best_streak,
        }
    except:
        session.close()
        return None


async def check_user_exists(user_id: int) -> bool:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        session.close()
        return user
    except:
        session.close()
        return False


async def increment_user_win(user_id: int) -> bool:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        user.win += 1
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False


async def increment_user_lose(user_id: int) -> bool:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        user.lose += 1
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False


async def increment_user_streak(user_id: int) -> bool:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        user.streak += 1
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False


async def reset_user_streak(user_id: int) -> bool:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        best_streak = user.streak
        user.streak = 0
        user.best_streak = best_streak
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False


async def increment_user_daily_win(user_id: int) -> bool:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        user.dwin += 1
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False


async def increment_user_daily_lose(user_id: int) -> bool:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        user.dlose += 1
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False


async def get_user_language(user_id: int) -> str:
    session = Session(engine)
    try:
        settings = session.query(Settings).filter(Settings.tgUserId == user_id).first()
        session.close()
        return settings.language
    except:
        session.close()


async def get_user_settings(user_id: int) -> dict | None:
    session = Session(engine)
    try:
        settings = session.query(Settings).filter(Settings.tgUserId == user_id).first()
        data = {
            "language": settings.language,
            "tries": str(settings.tries),
        }
        session.close()
        return data
    except:
        session.close()
        return None


async def update_user_language(user_id: int, language: str) -> bool:
    if language not in available_lang:
        return False
    session = Session(engine)
    try:
        settings = session.query(Settings).filter(Settings.tgUserId == user_id).first()
        settings.language = language
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False


async def update_user_tries(user_id: int, tries: str) -> bool:
    session = Session(engine)
    try:
        settings = session.query(Settings).filter(Settings.tgUserId == user_id).first()
        settings.tries = tries
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False


async def get_daily_words() -> dict | None:
    session = Session(engine)
    try:
        daily = session.query(Daily).order_by(Daily.date.desc()).first()
        session.close()
        if daily and daily.date == str(datetime.now().date()):
            return {
                "word_en": daily.word_en,
                "word_ru": daily.word_ru
            }
        return None
    except:
        session.close()
        return None


async def check_played_daily(user_id: int) -> bool:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        session.close()
        return user.completed_daily
    except:
        session.close()
        return False


async def played_daily_set(user_id: int) -> bool:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        user.completed_daily = 1
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False


async def reset_daily() -> bool:
    session = Session(engine)
    try:
        stmt = select(User).where(User.completed_daily == 1)
        for user in session.scalars(stmt):
            user.completed_daily = 0
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False
