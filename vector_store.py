import numpy as np

from embed_data import create_embeddings, embed


chunks, embeddings = create_embeddings()


class VectorStore:

    def __init__(self, chunks, embeddings):
        self.chunks = chunks
        self.embeddings = np.asarray(embeddings)

    def search(self, query_vec, k=4):
        scores = self.embeddings @ np.asarray(query_vec)

        top = np.argsort(-scores)[:k]

        return [
            (self.chunks[i], float(scores[i]))
            for i in top
        ]


store = VectorStore(chunks, embeddings)


def retrieve(question, k=4):
    query_vec = embed([question])[0]
    return store.search(query_vec, k=k)
