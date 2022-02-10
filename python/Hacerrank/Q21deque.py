from collections import deque
d = deque()
a = int(input())
k = ""
for i in range(a):
    b= input().split(" ")
    if len(b)>1:
        p = "d."+b[0]+"("+b[1]+")"
    else:
        p = "d."+b[0]+"()"
    eval(p)
print(*d)