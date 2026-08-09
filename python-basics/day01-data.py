import json
def print_documents_id_and_title(documents):
    for document in documents:
        print(f"Document ID: {document['id']}, Title: {document['title']}")

def print_total_num_documents(documents):
    print(f"Total number of documents: {len(documents)}")

def get_document_by_id(
        documents: list[dict], 
        doc_id: int
) -> dict | None:
    for document in documents:
        if document['id'] == doc_id:
            return document
    return None

def print_word_count_of_each_document(documents):
    for document in documents:
        word_count = len(document['content'].split())
        print(f"Document ID: {document['id']} has {word_count} words.")

def count_words(text:str) -> int:
    return len(text.split())

def summarize_documents(documents):
    summaries = []
    for document in documents:
        summary = {
            "id": document['id'],
            "title": document['title'],
            "word_count": count_words(document['content'])
        }
        summaries.append(summary)
    return summaries

def document_processing_report(documents: list[dict]):
    print("\nDocument Processing Report:")
    print("===========================")

    print(f"\nDocuments: {len(documents)}")
    count = 1
    word_count = 0
    for document in documents:
        print(f"\n{count}. {document['title']}")
        temp_word_count = count_words(document['content'])
        word_count += temp_word_count
        print(f"   Words: {temp_word_count}\n")
        count += 1

    print(f"\nTotal words: {word_count}")
    print(f"Average words per document: {word_count / len(documents) if documents else 0:.2f}")


with open('document.json', 'r') as file:
    documents = json.load(file)

document_processing_report(documents)