
n=int(input("enter the no"))
l1=0
l2=1
print(l1)
print(l2)
for a in range (2,n+1):
    l3=l1+l2
    print(l3)
    l1,l2=l2,l3
