# N= the number of customers 
# P = the number fo the products each customer brings
# jth product that the ith customer brings has a target of Xij pascals

from itertools import count


n = int(input())
for i in range(n):
    pressure = 0
    valprevious = 0
    n1,n2 = map(int,input().split())#n1 = size of outerarr and n2 = size of innerarr
    outerarr =[]
    for j in range(n1):
        innerarr = list(map(int,input().split()))
        outerarr.append(innerarr)
    for k in range(n1):
        c =0
        if(k>0):
            c = outerarr[k].count(valprevious) 
            if (c >=1):
                for _ in range (c):
                    outerarr[k].remove(valprevious)

        for l in range(n2-c):
            if(abs(valprevious-max(outerarr[k])) < abs(valprevious - min(outerarr[k]))):
                valcurrent = max(outerarr[k])
                pressure = pressure+ abs(valcurrent - valprevious)
                print("valuecurr",valcurrent,"pressure",pressure,"valpre",valprevious  , "max")
                valprevious = max(outerarr[k])
                outerarr[k].remove(max(outerarr[k]))
            elif(abs(valprevious-max(outerarr[k])) > abs(valprevious - min(outerarr[k]))):
                valcurrent = min(outerarr[k])
                pressure = pressure + abs(valprevious -valcurrent)
                print("valuecurr",valcurrent,"pressure", pressure,"valpre",valprevious ,"min")
                valprevious = min(outerarr[k])
                outerarr[k].remove(min(outerarr[k]))                  
    print(pressure)