# Given a sequence of characters your task is to count the number of times ACE is present.

# Output Format
# Single integer representing number of "ACE".
# Sample Input 
# ACEACE
# Sample Output 0
# 2

A = input("Enter Here-")
List = A.split()
count = 0
num = 0
for i in List:
    List2= list(i)
    if  len(List2)%3 == 0 and len(List2)!=3:
        for i in range(0,len(List2),3):
            if List2[0+i] == 'A':
                if List2[1+i] =='C':
                    if List2[2+i]=='E':
                        count = count +1
    
for i in range(len(List)):
    if List[i] == "ACE":
        count = count +1

print(count)