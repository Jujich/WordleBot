import logging

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


async def get_leaderboard() -> dict | None:
    session = Session(engine)
    try:
        res = {"games": "", "guess_rate": "", "longest_streak": ""}
        games = session.query(User).order_by((User.win + User.lose).desc()).all()[:5]
        streak = session.query(User).order_by((User.best_streak).desc()).all()[:5]
        guess_rate = session.query(User).order_by((User.win / (User.win + User.lose)).desc()).all()[:5]
        for i in range(5):
            try:
                res["games"] += f"<b>{i + 1}.</b> <i>{games[i].username}</i> - <b>{games[i].win + games[i].lose}</b>\n"
                res["guess_rate"] += f"<b>{i + 1}.</b> <i>{guess_rate[i].username}</i> - <b>{round((guess_rate[i].win / (guess_rate[i].win + guess_rate[i].lose)) * 100, 2) if guess_rate[i].win + guess_rate[i].lose != 0 else 0.0}%</b>\n"
                res["longest_streak"] += f"<b>{i + 1}.</b> <i>{streak[i].username}</i> - <b>{streak[i].best_streak}</b>\n"
            except IndexError:
                pass
        if res["games"] == "":
            res["games"] = None
        if res["guess_rate"] == "":
            res["guess_rate"] = None
        if res["longest_streak"] == "":
            res["longest_streak"] = None
        session.close()
        return res
    except Exception as e:
        logging.exception(e)
        session.close()
        return None


async def check_user_exists(user_id: int) -> bool:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        session.close()
        return user
    except Exception as e:
        logging.exception(e)
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
    except Exception as e:
        logging.exception(e)
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
    except Exception as e:
        logging.exception(e)
        session.close()
        return False


async def increment_user_streak(user_id: int) -> bool:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        user.streak += 1
        if user.streak > user.best_streak:
            user.best_streak = user.streak
        session.commit()
        session.close()
        return True
    except Exception as e:
        logging.exception(e)
        session.close()
        return False


async def reset_user_streak(user_id: int) -> bool:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        user.streak = 0
        if user.streak > user.best_streak:
            user.best_streak = user.streak
        session.commit()
        session.close()
        return True
    except Exception as e:
        logging.exception(e)
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
    except Exception as e:
        logging.exception(e)
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
    except Exception as e:
        logging.exception(e)
        session.close()
        return False


async def get_user_language(user_id: int) -> str:
    session = Session(engine)
    try:
        settings = session.query(Settings).filter(Settings.tgUserId == user_id).first()
        session.close()
        return settings.language
    except Exception as e:
        logging.exception(e)
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
    except Exception as e:
        logging.exception(e)
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
    except Exception as e:
        logging.exception(e)
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
    except Exception as e:
        logging.exception(e)
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
    except Exception as e:
        logging.exception(e)
        session.close()
        return None


async def check_played_daily(user_id: int) -> bool:
    session = Session(engine)
    try:
        user = session.query(User).filter(User.tgId == user_id).first()
        session.close()
        return user.completed_daily
    except Exception as e:
        logging.exception(e)
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
    except Exception as e:
        logging.exception(e)
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
    except Exception as e:
        logging.exception(e)
        session.close()
        return False
