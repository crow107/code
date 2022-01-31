from collections import namedtuple

A = int(input())
B = input()
Student = namedtuple('Student',B)
total = 0
for _ in range(A):
    student = Student(*input().split())
    total += (int(student.MARKS))
print('{:0.2f}'.format(total/A))