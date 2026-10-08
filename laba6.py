k=int(input())
s1="Мы нашли в лесу "
if k<0:
    print("Мы не находили грибы, а только теряли")
elif  11<=k<=19 or k%10==0 or k%10>4:
    print(s1+str(k)+" грибов")
elif 2<=k%10<=4:
    print(s1+str(k)+" гриба")
else:
    print(s1+str(k)+" гриб")
    
