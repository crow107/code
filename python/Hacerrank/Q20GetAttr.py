n = int(input())
b = map(int, input().split())
setb = set(b)
c = int(input())
for _ in range(c):
    d1,d2 = input().split()
    a =map(int,input().split())
    seta = set(a)
    getattr(setb,d1)(seta)
print(sum(setb))
# 👍good for using multiple commands at once

