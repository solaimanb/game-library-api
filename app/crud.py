from sqlalchemy.orm import Session
from . import models, schemas


def create_game(db: Session, game: schemas.GameCreate):
    db_game = models.Game(**game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).offset(skip).limit(limit).all()


def get_game_by_id(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()


def update_game(db: Session, game_id: int, game: schemas.GameCreate):
    db_game = get_game_by_id(db, game_id)
    if not db_game:
        return None

    for key, value in game.dict().items():
        setattr(db_game, key, value)

    db.commit()
    db.refresh(db_game)
    return db_game


def delete_game(db: Session, game_id: int):
    db_game = get_game_by_id(db, game_id)
    if not db_game:
        return None

    db.delete(db_game)
    db.commit()
    return True
