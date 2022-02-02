input()
array = input().split()
like = set(input().split())
dislike = set(input().split())
print(sum((i in like) - (i in dislike) for i in array))

# a = int(input())
# s = set()
# for i in range(a):
#     a = input()
#     s.add(a)
# print(len(s))