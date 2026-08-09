documents = [
    {
        "id": 1,
        "title": "Introduction to RAG",
        "content": "Retrieval Augmented Generation combines search with language models."
    },
    {
        "id": 2,
        "title": "Information Retrieval",
        "content": "Information retrieval is concerned with finding relevant information."
    },
    {
        "id": 3,
        "title": "Embeddings",
        "content": "Embeddings represent text as numerical vectors."
    }
]

print("Documents loaded successfully.")

for document in documents:
    print(f"Document ID: {document['id']}, Title: {document['title']}")

print("Total number of documents: ", len(documents))

print(f"Second document content: {documents[1]['content']}")

for document in documents:
    print(f"Word count of each document: {len(document['content'].split())} words in document ID: {document['id']}")