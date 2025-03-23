def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

if __name__ == "__main__":
    # Example usage
    text = "Your long subtitle text here..."
    chunks = chunk_text(text)
    print(chunks)