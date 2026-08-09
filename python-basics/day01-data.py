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


with open('document.json', 'r') as file:
    documents = json.load(file)
print("Documents loaded successfully.")
print_documents_id_and_title(documents)

print_total_num_documents(documents)

second_document = get_document_by_id(documents, 2)
if second_document:
    print(f"Second document content: {second_document['content']}")

summaries = summarize_documents(documents)
print("Document summaries:")
for summary in summaries:
    print(f"Document ID: {summary['id']}, Title: {summary['title']}, Word Count: {summary['word_count']}")