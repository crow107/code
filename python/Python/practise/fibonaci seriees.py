a=int(input("Enter the number:-"))
b=a
k=0
while b>0:
   c=b%10
   b=int(b/10)
   k=k+c**3
if k==a:
   print("yes")
else:
   print("no")

   
   
