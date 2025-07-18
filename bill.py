name=[]
qt=[]
pr=[]
n=0
ans=0
while True:
    a=input("enter a name of product(if nothing type x):")
    if a=='x':
        break;
    name.append(a)
    b=int(input("enter a quantity of product:"))
    qt.append(b)
    c=int(input("enter a price of product:"))
    pr.append(c)
    n+=1
print('='*50)
for i in range(0,n):
    temp=qt[i]*pr[i]
    ans+=temp
    print(name[i]," = $",temp)
print("total:$",ans)
print("="*50)
