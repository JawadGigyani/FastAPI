# Run from the backend folder:
#   pip install -r requirements.txt
#   copy .env.example to .env and add your keys
#   uvicorn app.main:app --reload
# Then open http://127.0.0.1:8000/docs

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.agent.graph import build_graph
from app.config import OUTPUT_DIR
from app.schemas import StoryRequest

# Build the LangGraph workflow once, when the server starts
graph = build_graph()

app = FastAPI(title="Voice Story Agent")

# Allow the frontend (running on a different address) to call this API
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Serve saved audio so you can play it in the browser: /audio/<file name>
app.mount("/audio", StaticFiles(directory=OUTPUT_DIR), name="audio")


# Create a narrated story  ->  POST /story
# REQUEST BODY (JSON): {"topic": "a robot who learns to paint"}
# RESPONSE: {"story": "...", "audio": "<mp3 as base64>"}
@app.post("/story")
def create_story(body: StoryRequest):
    result = graph.invoke({"topic": body.topic, "voice_id": body.voice_id})
    return {"story": result["story"], "audio": result["audio"]}


# Get all generated audio files  ->  GET /files
@app.get("/files")
def list_files():
    names = sorted(os.listdir(OUTPUT_DIR))
    return {"files": [f"/audio/{name}" for name in names]}
