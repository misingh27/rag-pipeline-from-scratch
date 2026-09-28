import ollama

from vector_store import retrieve


SYSTEM = (
    "You answer questions using only the provided context. "
    "If the answer is not in the context, say you do not know. "
    "Cite the sources you used by their number."
)


def build_prompt(question, retrieved):
    context = "\n\n".join(
        f"[{i + 1}] Source: {chunk['source']}\n{chunk['text']}"
        for i, (chunk, _score) in enumerate(retrieved)
    )

    return f"Context:\n{context}\n\nQuestion: {question}"


def answer_question(question, k=4):
    retrieved = retrieve(question, k=k)

    prompt = build_prompt(question, retrieved)

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def main():
    print("=" * 50)
    print("             DIY RAG ASSISTANT")
    print("=" * 50)
    print("Ask questions about your documents.")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("\nGoodbye!")
            break

        if not question:
            continue

        answer = answer_question(question)

        print(f"\nRAG: {answer}\n")


if __name__ == "__main__":
    main()
