from itertools import product

# EXAMPLE FOR PRODUCT FUNCTION AND LIST(MAP)
A = list(map(int ,input().split()))

B = list(map(int, input().split()))
p = list(product(A,B))
k = ''
for i in range(len(p)):
    k = k+str(p[i])+' '

print(k)
