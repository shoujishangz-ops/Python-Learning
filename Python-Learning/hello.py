name = input("请输入用户名:")
age = int(input("请输入年龄:"))

if age >= 18:
    print(f"你好,{name},你可以使用AI助手")
else:
    print(f"你好,{name},你暂时不能使用AI助手")