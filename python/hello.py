n = int(input)
arr = map(int,n.split())
Arr= list(arr)
l = max(Arr)
k =''
while l in Arr:
    Arr.remove(l)
for i in range(len(Arr)):
    k = k+ str(Arr[i])+' ' 
print(k)