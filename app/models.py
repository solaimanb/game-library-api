from sqlalchemy import Boolean, Column, Integer, String, Float, Enum as SQLAlchemyEnum
from .database import Base
from .schemas import GameCategory


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True, nullable=False)
    category = Column(SQLAlchemyEnum(GameCategory), nullable=False)
    release_year = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    is_multiplayer = Column(Boolean, default=False, nullable=False)

    class Config:
        from_attributes = True
