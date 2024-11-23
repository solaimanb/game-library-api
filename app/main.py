from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from . import models, schemas, crud
from .database import engine, get_db
from .schemas import GameCategory

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Game Library API",
    description="A simple API for managing a game library",
)

# CORS Middleware --->
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# GET ROOT --->
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Gracias por usar - Game Library API!"}


# CREATE GAME --->
@app.post("/games/", response_model=schemas.Game, tags=["Games"])
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    return crud.create_game(db=db, game=game)


# GET ALL GAMES --->
@app.get("/games/", response_model=List[schemas.Game], tags=["Games"])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_games(db, skip=skip, limit=limit)


# GET GAME BY ID --->
@app.get("/games/{game_id}", response_model=schemas.Game, tags=["Games"])
def read_game(game_id: int, db: Session = Depends(get_db)):
    db_game = crud.get_game_by_id(db, game_id=game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game


# UPDATE GAME --->
@app.put("/games/{game_id}", response_model=schemas.Game, tags=["Games"])
def update_game(game_id: int, game: schemas.GameCreate, db: Session = Depends(get_db)):
    update_game = crud.update_game(db, game_id, game)
    if update_game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return update_game


# GET ALL CATEGORIES --->
@app.get("/game-categories")
def get_game_categories():
    return [category.value for category in GameCategory]


# DELETE GAME --->
@app.delete("/games/{game_id}", tags=["Games"])
def delete_game(game_id: int, db: Session = Depends(get_db)):
    success = crud.delete_game(db, game_id)
    if not success:
        raise HTTPException(status_code=404, detail="Game not found")
    return {"message": "Game deleted successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
