from collections import Counter
a = int(input())
s=[]
for i in range(a):
    p = input()
    s.append(p)
b = Counter(s).values()
print(len(b))
print (*b)
    
