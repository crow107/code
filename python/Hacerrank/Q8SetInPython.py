def average(array):
    a = set(arr)
    length_a = len(a)
    k = list(a)
    c = 0
    for i in range (length_a):
        b = k[i]
        c = c+b
    result= c/length_a  
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)