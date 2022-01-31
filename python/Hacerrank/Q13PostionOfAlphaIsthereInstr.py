a,b =map(int,input().split())
grA = []
count =0
for i in range(a):
    k = input()
    grA.append(k)
for j in range(b):
    s =  input()
    if s in grA:
        for i in range(len(grA)):
            if grA[i]==s:
                print(str(i+1)+' ',end ='')
        print('')
    
    else:
        print("-1")
        
                