from itertools import permutations

S,K = input().split()

s = str(S)
k = int(K)
ka = ''
Permutation = list(permutations(s,k))
SPermutation = sorted(Permutation)
for i in range(len(Permutation)):
    a =''.join(SPermutation[i])
    ka = ka +  a
    print(ka)
    ka =''
