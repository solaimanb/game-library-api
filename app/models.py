from sqlalchemy import Boolean, Column, Integer, String, Float
from .database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    category = Column(String)
    release_year = Column(Integer)
    rating = Column(Float)
    is_multiplayer = Column(Boolean, default=False)
