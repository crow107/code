def Design(N,M):
    # top cone 
    a = ".|."
    n = (N-1)//2
    m = (M-3)//2
    
    for i in range(n):
        print((a*i).rjust(m,"-")+a+(a*i).ljust(m,"-"))
    #WELCOME
    print(("WELCOME").center(M,"-"))
    #bottom cone
    for i in range(n):
        print((a*(n-i-1)).rjust(m,"-")+a+(a*(n-i-1)).ljust(m,"-"))

    

if __name__ == '__main__':
    N,M = input().split()
    n = int(N)
    m = int(M)
    design = Design(n,m)
    