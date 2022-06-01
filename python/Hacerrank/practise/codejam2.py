# print("Case #"+str(case)+": "+str(var))

# N number of elements of the inital list
# K maximum number of elements can be added

case = 1
n = int(input())
for i in range(n):
    N,K = map(int,input().split())
    E = list(map(int,input().split()))
    Sum =0
    SquareSum =0
    count = 0
    for i in range (N):
        if E[i]!=0:
            Sum += E[i]
            SquareSum +=(E[i])**2
        else:
            count += 1
    


    if(K == 1 and Sum!=0 ):
        if(SquareSum-(Sum**2))%(Sum*2)==0:
            x = int((SquareSum-(Sum**2))/(Sum*2))
            print("Case #"+str(case)+": "+str(x))
        else:
            print("Case #"+str(case)+": IMPOSSIBLE")
        

        case += 1
    elif(count==N):
        print("Case #"+str(case)+": 1")
        case +=1
    else:
        print("Case #"+str(case)+": IMPOSSIBLE")
        case +=1
