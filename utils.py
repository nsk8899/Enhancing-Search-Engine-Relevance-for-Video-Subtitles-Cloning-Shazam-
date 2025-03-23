import ffmpeg
import whisper
import numpy as np
import os
import re

# Function to Extract Audio from Video
def extract_audio(video_path):
    """Extracts audio from the video and saves it as a WAV file."""
    audio_path = video_path.replace(".mp4", ".wav")
    ffmpeg.input(video_path).output(audio_path, format='wav', acodec='pcm_s16le').run()
    return audio_path

# Function to Transcribe Audio to Subtitles (Using Whisper)
def transcribe_audio(audio_path, srt_path="backend/subtitles.srt"):
    """Transcribes audio using Whisper and saves subtitles to an SRT file."""
    model = whisper.load_model("base")  # Use "small" or "medium" for better accuracy
    result = model.transcribe(audio_path)
    
    # Save transcription to an SRT file
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result["segments"]):
            start = format_time(segment["start"])
            end = format_time(segment["end"])
            text = segment["text"]
            f.write(f"{i+1}\n{start} --> {end}\n{text}\n\n")
    
    return srt_path

# ✅ Function to Convert Time Format for SRT
def format_time(seconds):
    """Formats time in HH:MM:SS,ms format for SRT."""
    millisec = int((seconds % 1) * 1000)
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{millisec:03}"

# Function to Search in SRT File Instead of FAISS
def search_subtitles(query, srt_file="backend/subtitles.srt"):
    """Searches for a query in an SRT file and returns matching subtitle blocks."""
    results = []
    
    # Open and read the SRT file
    with open(srt_file, "r", encoding="utf-8") as f:
        subtitles = f.read()
    
    # Split subtitles based on timestamp blocks
    subtitle_blocks = subtitles.split("\n\n")

    # Search for the query in subtitles
    for block in subtitle_blocks:
        if query.lower() in block.lower():
            results.append(block.strip())

    return results if results else ["No matching subtitles found."]

# Function to Generate Embeddings (Using Random Numbers for Now)
def generate_embeddings(text):
    """Generates dummy embeddings (Replace with Gemini API if needed)."""
    return np.random.rand(1, 512).astype("float32")

# Function to Run Full Pipeline
def process_video(video_path="videos/sample_video.mp4"):
    """Runs the full process: Extract audio, transcribe, and save subtitles."""
    if not os.path.exists(video_path):
        return "❌ Error: Video file not found!"
    
    print("🔹 Extracting audio...")
    audio_path = extract_audio(video_path)

    print("🔹 Transcribing audio to subtitles...")
    srt_path = transcribe_audio(audio_path)

    print(f" Done! Subtitles saved at: {srt_path}")

# Testing the Full Process
if __name__ == "__main__":
    video_path="videos/sample_video.mp4"
    process_video()  # Runs full pipeline
    query = "hello"  # Example query
    print("\n🔎 Search Results:", search_subtitles(query))
    