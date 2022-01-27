from itertools import combinations
S,K = input().split()

s = str(S)
Ss = sorted (s)
k = int(K)
ka = ''
for A in range(1,k+1):
    Combination = list(combinations(Ss,A))
    for i in range(len(Combination)):
        a =''.join(Combination[i])
        ka = ka + a
        print(ka)
        ka =''

