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
    streak: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    best_streak: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"User(id={self.id}, tgId={self.tgId}, username={self.username}, win={self.win}, lose={self.lose}, games={self.games}, streak={self.streak}, best_streak={self.best_streak})"
