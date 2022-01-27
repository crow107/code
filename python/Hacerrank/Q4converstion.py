def print_formatted(N):
    def prepend(s,l):
        d = l - len(s)
        return d*" " + s
    maxlen = len(bin(N))-2

    for i in range(1,N+1):
        binary = prepend(bin(i)[2:],maxlen)
        decimal = prepend(str(i),maxlen)
        octal = prepend(oct(i)[2:],maxlen)
        hexdec = prepend(hex(i)[2:].upper(),maxlen)
        print(decimal + " " + octal + " " + hexdec + " " + binary)
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)