documents=[
    {
        "name":"Python基础",
        "score":0.9
    },
    {
        "name":"Git教程",
        "score":0.7
    },
    {
        "name":"RAG原理",
        "score":0.95
    }
]
result={
    doc["name"]:"优秀"
    for doc in documents
    if doc["score"] >= 0.8
}
for key,value in result.items():
    print(f"{key}:{value}")
