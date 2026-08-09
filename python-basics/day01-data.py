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

def print_documents_id_and_title(documents):
    for document in documents:
        print(f"Document ID: {document['id']}, Title: {document['title']}")

def print_total_num_documents(documents):
    print(f"Total number of documents: {len(documents)}")

def get_document_by_id(documents, doc_id):
    for document in documents:
        if document['id'] == doc_id:
            return document
    return None

def print_word_count_of_each_document(documents):
    for document in documents:
        word_count = len(document['content'].split())
        print(f"Document ID: {document['id']} has {word_count} words.")

print("Documents loaded successfully.")
print_documents_id_and_title(documents)

print_total_num_documents(documents)

second_document = get_document_by_id(documents, 2)
if second_document:
    print(f"Second document content: {second_document['content']}")

print_word_count_of_each_document(documents)