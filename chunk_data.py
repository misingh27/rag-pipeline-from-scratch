from load_data import load_documents, clean


def chunk_text(text):
    paragraphs = text.split("\n\n")

    chunks = []

    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        if paragraph:
            chunks.append(paragraph)

    return chunks


def create_chunks(folder="docs"):
    docs = load_documents(folder)

    for doc in docs:
        doc["text"] = clean(doc["text"])

    chunks = []

    for doc in docs:
        for text in chunk_text(doc["text"]):
            chunks.append({
                "text": text,
                "source": doc["source"]
            })

    return chunks


if __name__ == "__main__":
    chunks = create_chunks()
    print(f"Split documents into {len(chunks)} chunks")
