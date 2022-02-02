from collections import Counter
A = []
K = int(input())
for _ in range(K):
    a,s,b = input().rpartition(" ")
    B =[]
    p = 0
    for j in range(len(A)):
        if a in A[j][0]:
            A[j][1]= int(A[j][1])+int(b)
            p = 1
    if p !=1:
        B.append(a)
        B.append(b)
        A.append(B)
for i in range (len(A)):
    print(A[i][0],A[i][1])

