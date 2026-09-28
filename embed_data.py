from sentence_transformers import SentenceTransformer

from chunk_data import create_chunks


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def embed(texts):
    return model.encode(
        texts,
        normalize_embeddings=True
    )


def create_embeddings(folder="docs"):
    chunks = create_chunks(folder)
    chunk_texts = [chunk["text"] for chunk in chunks]

    embeddings = embed(chunk_texts)

    return chunks, embeddings


if __name__ == "__main__":
    chunks, embeddings = create_embeddings()

    print(f"Created embeddings with shape: {embeddings.shape}")
