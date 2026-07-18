documents=[
    {"name":"Python","score":0.9},
    {"name":"Java","score":0.4},
    {"name":"RAG","score":0.8}
]
document = [
    document["name"]
    for document in documents
    if document["score"] >= 0.7
]
print(document)