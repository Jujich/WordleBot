from db.classes import User
from db.engine import engine
from sqlalchemy.orm import Session


async def insert_user(user_id: int, username: str) -> bool:
    session = Session(engine)
    try:
        user = User(
            tgId=user_id,
            username=username,
        )
        session.add(user)
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
