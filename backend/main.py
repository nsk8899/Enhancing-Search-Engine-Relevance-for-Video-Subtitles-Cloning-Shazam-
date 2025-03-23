from fastapi import FastAPI, UploadFile, File
from backend.utils import extract_audio, generate_embeddings, search_subtitles
import os

app = FastAPI()

@app.post("/upload_video/")
async def upload_video(file: UploadFile = File(...)):
    file_location = f"videos/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    extract_audio(file_location)
    return {"message": "Video uploaded and processed."}

@app.get("/search/")
def search(query: str):
    results = search_subtitles(query)
    return {"results": results}
