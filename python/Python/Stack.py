def Push(stk,item):
   stk.append(item)
   top=len(stk)-1
def isEmpty(stk):
   if stk==[]:
      return True
   else:
      return False
   
def Display(stk):
   if isEmpty(stk):
      print("Stack empty")
   else:
      top=len(stk)-1
      print(stk[top],'<-top')
   



Stack=[]
top=None
while True:
   print('STACK OPERATIONS')
   print('1.PUSH')
   print('2.DISPLAY')
   print('3.Exit')
   a=int(input("Enter here:- "))
   if a==1:
      no=int(input("Enter the rollno"))
      name=input("Enter name ")
      item=[no,name]
      Push(Stack,item)
      input()
   elif a==2:
      Display(Stack)
      input()
   elif a==3:
      break
   else:
      print('ERROR')
