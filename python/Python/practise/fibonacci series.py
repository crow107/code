org=int(input("enter the number"))
rev=0
while org>0:
   a=org%10
   rev=rev*10+a
   org=org//10
print(rev)   
