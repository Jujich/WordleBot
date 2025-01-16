from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tgId: Mapped[int] = mapped_column(Integer, unique=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    win: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    lose: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    dwin: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    dlose: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    streak: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    best_streak: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    completed_daily: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"User(id={self.id}, tgId={self.tgId}, username={self.username}, win={self.win}, lose={self.lose}, streak={self.streak}, best_streak={self.best_streak})"


class Settings(Base):
    __tablename__ = 'settings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tgUserId: Mapped[int] = mapped_column(Integer, ForeignKey('users.tgId'))
    language: Mapped[str] = mapped_column(String(50), nullable=False, default='en')
    tries: Mapped[str] = mapped_column(String, nullable=False, default=6)

    def __repr__(self):
        return f"Settings(id={self.id}, tgId={self.tgUserId}, language={self.language})"


class Daily(Base):
    __tablename__ = 'dailies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[str] = mapped_column(String(50), nullable=False)
    word_en: Mapped[str] = mapped_column(String(50), nullable=False)
    word_ru: Mapped[str] = mapped_column(String(50), nullable=False)

    def __repr__(self):
        return f"Daily(id={self.id}, word_en={self.word_en}, word_ru={self.word_ru}, date={self.date})"
