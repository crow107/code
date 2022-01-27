import string
def print_rangoli(size):
    n = 0
    alphabet_str = string.ascii_lowercase
    alpha = list(alphabet_str)
    # top cone
    for j in range(0,size):
        side = (size*2-2)
        print ((j*(alpha[size-j]+"-")).rjust(side,"-") + alpha[size] +(j*("-"+alpha[size-j])).ljust(side,"-"))
    for j in range(size-2,-1,-1):
        side = (size*2-2)
        print ((j*(alpha[size-j]+"-")).rjust(side,"-") + alpha[size] +(j*("-"+alpha[size-j])).ljust(side,"-"))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)