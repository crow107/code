n1 = int(input())
s1 = map(int,input().split())
n2 = int(input())
s2 = map(int,input().split())

#set -> union , intersection, difference , symmetric_difference.
s = set(s1)
k = s.intersection(s2)
count = 0
count2 = 0
p = s.union(s2)
for i in k:
    count = count +1
print(count)
for i in p:
    count2= count2+1