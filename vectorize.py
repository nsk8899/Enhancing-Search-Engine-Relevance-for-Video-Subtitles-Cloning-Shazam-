from sentence_transformers import SentenceTransformer
import pandas as pd

def vectorize_subtitles(cleaned_df):
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Load a pre-trained model
    embeddings = model.encode(cleaned_df['cleaned_text'].tolist())
    return embeddings

if __name__ == "__main__":
    cleaned_df = pd.read_csv('data/cleaned_subtitles.csv')
    embeddings = vectorize_subtitles(cleaned_df)
    # Save embeddings to a file or database