# --- -----------------------------
#solution
# N+1 bounce
#D1 = 0 
#D2 = D1 + L1 , D2 = L1
#D3 = L1 + L2
#Dn = L1 + L2 +L3 +...+Ln
# N X
# L1 L2 L3 ...LN
# Dn <= X to find the number of times the ball will make a bounce where the coordinate is at most X 

N,X = input().split(" ")
L = input().split(" ")
D1 = 0
n = int(N)
x = int(X)
Dn = list(L)
for i in range(len(Dn)):
    D1 = D1 + int(Dn[i])
    if D1<=x:
        bounceAtMostXCoordinate = D1
        bounceAtMostX = i+2 # +2 because {+1 for correcting i value (i can be zero)} {+1 because we have given that ball is making N+1 bounces}

print("Number of time ball bounce is =>",bounceAtMostX," where corrdinate is  =>",bounceAtMostXCoordinate)


