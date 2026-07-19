documents=[
    {
        "name":"Python基础",
        "category":"编程",
        "score":0.9
    },
    {
        "name":"Git教程",
        "category":"工具",
        "score":0.7
    },
    {
        "name":"RAG原理",
        "category":"AI",
        "score":0.95
    }
]
for document in documents:
    if document["score"] >= 0.8:
        document["level"] = "优秀"
    else:
        document["level"] = "普通"

result = {
    document["name"]:document["level"]
    for document in documents
}
for i,document in enumerate(documents,start=1):
    print(f"文档{i}:")
    for key,value in document.items():
        print(f"{key}:{value}")
    print()

