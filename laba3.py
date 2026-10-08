a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    print("Да")
    if a==b==c:
        print("Равносторонний")
    elif a==b or b==c or a==c:
        print("Равнобедренный")
    else:
        print("Разносторонний")
else:
    print("Нет")
