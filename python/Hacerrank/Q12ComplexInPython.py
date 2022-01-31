import cmath
s = input()
try:
    a,b = s.split("+")
except:
    a,b = s.split("-")


for i in b:
    try :
        int(i)
        if True:
            b =i
    except:
        pass
A = int(a)
B = int(b)
print(abs(complex(A,B)))
print(cmath.phase(complex(A,B)))

