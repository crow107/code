print("1= a3-b3 = (a-b)(a2+b2+ab)")
print("2= a3+b3 = (a+b)(a2+b2-ab)")
x=int(input("write the value of a = "))
y=int(input("write the value of b = "))
i=int(input("If you want to choose :- a3-b3 = (a-b)(a2+b2+ab) press == 1=== if not press 2==="))
j=int(input("Or if you want to choose :- a3+b3 = (a+b)(a2+b2-ab) press == 2=== if not press 3==="))
o = x*x*x+y*y*y
k = x*x*x-y*y*y
if i < 2 :
    print(o)
if j < 3 :
    print(k)
