# you are inside  building a tower of letter blocks
# letter block is wooden cube
# letter on one side
# print("Case #"+str(case)+": "+str(var))


from typing import final


case = 1
n = int(input())
for i in range(n):
    num_tower = int(input())
    outerlist = []
    count = 0
    outerfullist =[]
    S = list(input().split())
    for j in range (num_tower):
        innerlist =[]
        outerfullist.append(S[j])
        
        for k in S[j]:
            innerlist.append(k)
        outerlist.append(innerlist)
    finallist = ""
    for j in range (num_tower):
        for k in range(num_tower):
            if(k!=j):
                