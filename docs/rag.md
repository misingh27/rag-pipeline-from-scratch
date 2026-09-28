# Retrieval Augmented Generation

Retrieval Augmented Generation, commonly called RAG, is a technique that combines information retrieval with language generation.

A typical RAG system first stores documents in an indexed representation. When a user asks a question, the system searches the indexed documents for relevant content.

Documents are usually divided into smaller pieces called chunks. Chunking allows the retrieval system to identify specific sections that are relevant to a question instead of retrieving an entire document.

An embedding model converts text into numerical vectors. Texts with similar meanings tend to have embeddings that are close to each other in vector space.

During retrieval, the query is converted into an embedding and compared with document chunk embeddings. Similarity measures such as cosine similarity can be used to identify relevant chunks.

The retrieved chunks are then provided to a language model as context. The language model uses the question and retrieved context to generate an answer.

A basic RAG pipeline can therefore be described as document loading, text cleaning, chunking, embedding, indexing, retrieval, prompt construction, and generation.

RAG can help ground language model responses in a specific collection of information. It is particularly useful when the relevant information is not contained in the model's original training data or when answers need to reference a private or changing knowledge base.

Retrieval quality is important in RAG. If the system retrieves irrelevant or incomplete information, the generated answer may also be poor even when the language model itself is capable.
