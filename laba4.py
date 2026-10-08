x=int(input())
y=int(input())
if x**2+y**2<=1 or (y<0 and x<0 and y>-x-2):
    print("Да")
else:
    print("Нет")
