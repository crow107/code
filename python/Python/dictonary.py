
n=int(input("ENTER THE NUMBER OF EMPLOYS:-"))
a=1
b=1
p=dict()
l=dict()
while a<=n:
   nm=input("ENTER THE NAME OF EMPLOY:-")
   dn=input("ENTER THE DESIGNATION:-")
   l[a]=nm
   p[a]=dn
   a=a+1
print('S.NO''\t\t','NAME''\t\t','DESIGNATION')
while b<=n:
   print(b,'\t\t',l[b],'\t\t',p[b]) 
   b=b+1 
