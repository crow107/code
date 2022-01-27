t=tuple()
l=tuple()
a=1
k=int(input("ENTER THE NUMBER OF FRUITS:-"))
while a<=k:
   q=input("ENTER THE NAME OF FRUIT:-")
   w=int(input("ENTER THE PRICE OF FRUIT:-"))
   t+=(q,)
   l+=(w,)
   a=a+1
print('S.NO''\t\t','NAME OF FRUIT''\t\t','PRICE')
for p in range(0,k):
   print(p,'\t\t\t',t[p],'\t\t\t',l[p])



   

