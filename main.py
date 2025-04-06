from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel, Field, StringConstraints
import motor.motor_asyncio
from typing import List, Annotated
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

MONGO_URI = os.getenv("MONGO_URI")

# Connect to Mongo Atlas
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.multimedia_db

class PlayerScore(BaseModel):
    player_name: Annotated[
        str,
        StringConstraints(
            min_length=1,
            max_length=30,
            pattern=r"^[a-zA-Z0-9_ ]+$"
        )
    ]
    score: Annotated[int, Field(ge=0, le=1000000)]

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI!"}


@app.post("/upload_sprite")
async def upload_sprite(file: UploadFile = File(...)):
    # In a real application, the file should be saved to a storage service
    content = await file.read()
    sprite_doc = {"filename": file.filename, "content": content}
    result = await db.sprites.insert_one(sprite_doc)
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}

@app.get("/sprites", response_model=List[dict])
async def get_sprites():
    """Retrieves all uploaded sprites."""
    sprites = await db.sprites.find().to_list(100)
    return [{"id": str(sprite["_id"]), "filename": sprite["filename"]} for sprite in sprites]

@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    content = await file.read()
    audio_doc = {"filename": file.filename, "content": content}
    result = await db.audio.insert_one(audio_doc)
    return {"message": "Audio file uploaded", "id": str(result.inserted_id)}


@app.get("/audio", response_model=List[dict])
async def get_audio():
    """Retrieves all uploaded audio files."""
    audio_files = await db.audio.find().to_list(100)
    return [{"id": str(audio["_id"]), "filename": audio["filename"]} for audio in audio_files]


@app.post("/player_score")
async def add_score(score: PlayerScore):
    score_doc = score.dict()
    result = await db.scores.insert_one(score_doc)
    return {"message": "Score recorded", "id": str(result.inserted_id)}

@app.get("/scores", response_model=List[dict])
async def get_scores():
    """Retrieve all player scores and sorted by highest score."""
    scores = await db.scores.find().sort("score", -1).to_list(100)
    return [{"player_name": score["player_name"], "score": score["score"]} for score in scores]
