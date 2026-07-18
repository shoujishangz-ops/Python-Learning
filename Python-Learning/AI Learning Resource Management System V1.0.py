documents = [
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
    },
    {
        "name":"Agent开发",
        "category":"AI",
        "score":0.85
    }
]
def show_documents(documents):
    for i,document in enumerate(documents,start=1):
        print(f"资料{i}:")
        print(f"名称:{document["name"]}")
        print(f"分类:{document["category"]}")
        print(f"评分:{document["score"]}")

def add_documents(documents):
    new_name = input("请输入资料名称:")
    new_category = input("请输入资料分类:")
    new_score = float(input("请输入资料评分:"))
    new_document = {
        "name": new_name,
        "category": new_category,
        "score": new_score
    }
    documents.append(new_document)
    print("添加成功")

def delete_documents(documents):
    delete_name = input("请输入删除的资料名称:")
    for document in documents:
        if document["name"] == delete_name:
            documents.remove(document)
            print("删除成功")
            return
    
    print("没有找到该资料")

def judge_documents(documents):
    good_documents = [
        document["name"]
        for document in documents
        if document["score"] >= 0.8]
    
    for good_document in good_documents:
        print(good_document)

def search_documents(documents):
    search_document = input("请输入关键词:")
    for document in documents:
        if document["category"] == search_document:
            print(document["name"])

def get_score(document):
    return document["score"]

def sort_documents(documents):
    documents.sort(
        key = get_score,
        reverse = True
    )
    for document in documents:
        print(document["name"],document["score"])

def main():
    while True:
        print("====== AI学习资料管理器 ======")
        print("1. 查看所有资料")
        print("2. 添加学习资料")
        print("3. 删除学习资料")
        print("4. 查看高质量资料")
        print("5. 搜索AI资料")
        print("6. 按评分排序")
        print("7. 退出")
        num = input("请输入操作编号:")
        if num == "1":
            show_documents(documents)
        elif num =="2":
            add_documents(documents)
        elif num =="3":
            delete_documents(documents)
        elif num =="4":
            judge_documents(documents)
        elif num =="5":
            search_documents(documents)
        elif num =="6":
            sort_documents(documents)
        elif num =="7":
            print("退出成功")
            break
        else:
            print("输入编号有误，请重新输入")
main()