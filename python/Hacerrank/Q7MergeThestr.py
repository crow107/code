def merge_the_tools(string, k):
    t =[]
    c =''
    u =''
    n = len(string)
    for s in range(0,n,k):
        t.append(string[s:s+k])
    for i in range(len(t)):
        for j in range(k):
            if t[i][j] not in c:
                c = c +t[i][j]
                u = u +t[i][j]
        c = ''
        print(u)
        u = ''
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)