from pathlib import Path
import re


def load_documents(folder):
    docs = []

    for path in Path(folder).rglob("*"):
        if path.suffix.lower() in {".md", ".txt"}:
            text = path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            docs.append({
                "source": str(path),
                "text": text
            })

    return docs


def clean(text):
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


if __name__ == "__main__":
    docs = load_documents("docs")

    for doc in docs:
        doc["text"] = clean(doc["text"])

    print(f"Loaded {len(docs)} documents")

    for doc in docs:
        print(f"- {doc['source']}")
