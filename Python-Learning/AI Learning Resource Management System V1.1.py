def print_document(document):
    for key,value in document.items():
        print(f"{key}:{value}")
    print()

def print_documents(documents):
    for document in documents:
        print_document(document)
        
def add_level(documents):
    for document in documents:
        document["level"] = ("优秀" if document["score"] >=0.8 else "普通")

def show_documents(documents):
    for i,document in enumerate(documents,start=1):
        print(f"资料{i}:")
        print_document(document)
       
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
    add_level(documents)
    print("添加成功")


def delete_documents(documents):
    deleted = False
    delete_name = input("请输入删除的资料名称:")
    new_documents = []
    
    for document in documents:
        if document["name"] == delete_name:
            deleted = True
        else:
            new_documents.append(document)

    if deleted == True:
        print("删除成功")
    else:
        print(f"删除失败，没有找到{delete_name}")
    return new_documents
    

def judge_documents(documents):
    good_documents = [
        document
        for document in documents
        if document.get("level") == "优秀"]
    
    print_documents(good_documents)

def search_documents(documents):
    search_document = input("请输入关键词:")
    result = [
        document
        for document in documents
        if search_document in document["category"]
        or search_document in document["name"]
    ]
    print_documents(result)
    
def get_score(document):
    return document["score"]

def sort_documents(documents):
    documents.sort(
        key = get_score,
        reverse = True
    )
    for document in documents:
        print(document["name"],document["score"])

def show_menu():
    print("====== AI学习资料管理器 ======")
    print("1. 查看所有资料")
    print("2. 添加学习资料")
    print("3. 删除学习资料")
    print("4. 查看高质量资料")
    print("5. 搜索资料")
    print("6. 按评分排序")
    print("7. 退出")
def main():
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
    add_level(documents)
    while True:
        show_menu()
        num = input("请输入操作编号:")
        if num == "1":
            show_documents(documents)
        elif num =="2":
            add_documents(documents)
        elif num =="3":
            documents = delete_documents(documents)
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