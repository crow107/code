# N = number or cities
# M = Flights connections
# 1 city = Noob Land 
# Nth city = Ace land
# M lines are describing the flights.
# A B C
# A = Flight begins at city a 
# B =Flight ends at city b
# C = price 
# Q.
# 3 4
# 1 2 3
# 2 3 1
# 1 3 7
# 2 1 5

# N = 3 (3 cities)[1 2 3]
# M = 4 (4 connection) {(1->2)(2->3)(1->3)(2->1)}
# Price={(1->2):(3) , (2->3):(1) , (1->3):(7) , (2->1):(5)}

# Output Format-
# The cheapest route from "Noob Land" TO "Ace Land" 



# Solution - 


Dict = {}
def dic(a,b,c):
    dic2 = {(a,b):c}
    Dict.update(dic2)
def pricelessthan3City(l,n):
    global count
    global list2
    count = 0
    list1= []
    list2 = [] 
    for i in range(1,l+1):
        list1.append(i)
    r = 0
    while r<l:
        try:
            count = count + Dict[(list1[r],list1[r+1])]
            list2.append(Dict[(list1[r],list1[r+1])])
        except:
            return
        r = r + 1
    
# def for4orMoreCity():


    
N,M = input().split(" ")
n = int(N)
m = int(M)
for i in range(m):
    A,B,C = input().split(" ")
    a = int(A)
    b = int(B)
    c = int(C)
    dic(a,b,c)


for l in range(2,n+1):
    pricelessthan3City(l,n)
if a <=3:
    pricefrom1ToN = Dict[(1,n)]
    if pricefrom1ToN//2>=(max(list2)//2+count-max(list2)):
        print(max(list2)//2+count-max(list2))
    elif pricefrom1ToN//2<(max(list2)//2+count-max(list2)):
        print(pricefrom1ToN//2)

# if a >3:
    

