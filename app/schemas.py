from enum import Enum
from pydantic import BaseModel, Field


class GameCategory(str, Enum):
    ACTION = "action"
    STRATEGY = "strategy"
    RPG = "rpg"
    SPORTS = "sports"
    FIGHTING = "fighting"
    SIMULATION = "simulation"
    ADVENTURE = "adventure"
    RACING = "racing"
    SHOOTER = "shooter"
    PUZZLE = "puzzle"
    PLATFORM = "platform"
    EDUCATIONAL = "educational"
    CARD = "card"
    BOARD = "board"
    CASINO = "casino"
    MUSIC = "music"
    ARCADE = "arcade"
    TRAINING = "training"
    QUIZ = "quiz"
    FAMILY = "family"
    FUTURES = "futures"
    PARTY = "party"
    SANDBOX = "sandbox"
    OTHER = "other"


class GameBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=100)
    category: GameCategory
    release_year: int = Field(..., gt=1970, lt=2024)
    rating: float = Field(..., ge=0, le=10)
    is_multiplayer: bool = False


class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: int

    class Config:
        orm_mode = True
