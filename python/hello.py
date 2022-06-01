a = int(input())
case = 1
def mini(a,b,c):
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    elif c<=a and c<=b:
        return c
    else : 
        return 1

for i in range (a):
    num1a,num1b,num1c,num1d = map(int,input().split())
    num2a,num2b,num2c,num2d = map(int,input().split())
    num3a,num3b,num3c,num3d = map(int,input().split())
    nums = [mini(num1a,num2a,num3a),mini(num1b,num2b,num3b),mini(num1c,num2c,num3c),mini(num1d,num2d,num3d)]
    if nums[0]+nums[1]+nums[2]+nums[3]==1000000:
        print("Case #"+str(case)+": "+ str(nums[0]) +" "+str(nums[1])+" "+str(nums[2])+" "+str(nums[3]))
    elif nums[0]+nums[1]+nums[2]+nums[3] <1000000:
        print("Case #"+str(case)+": IMPOSSIBLE")
    elif nums[0]+nums[1]+nums[2]+nums[3] >1000000:
        while(nums[0]+nums[1]+nums[2]+nums[3]!=1000000):
            if(nums[-1]>=nums[0]+nums[1]+nums[2]+nums[3]-1000000):
                nums[-1] = nums[-1] - (nums[0]+nums[1]+nums[2]+nums[3]-1000000)

            elif(nums[-1]+nums[-2] >= (nums[0]+nums[1]+nums[2]+nums[3]-1000000)):
                nums[-2] = nums[-2]-((nums[0]+nums[1]+nums[2]+nums[3]-1000000)-nums[-1])
                nums[-1] =0

            elif(nums[-1]+nums[-2]+nums[-3] >= (nums[0]+nums[1]+nums[2]+nums[3]-1000000)):
                nums[-3] = nums[-3]-((nums[0]+nums[1]+nums[2]+nums[3]-1000000) - nums[-1] - nums[-2])
                nums[-1] =0
                nums[-2] =0

            elif(nums[-1]+nums[-2]+nums[-3]+nums[-4] >= (nums[0]+nums[1]+nums[2]+nums[3]-1000000)):
                nums[-4] =nums[-4]- ((nums[0]+nums[1]+nums[2]+nums[3]-1000000) - nums[-3] - nums[-2] -nums[-1])
                nums[-1] =0
                nums[-2] =0
                nums[-3] =0

            print("Case #"+str(case)+": "+ str(nums[0]) +" "+str(nums[1])+" "+str(nums[2])+" "+str(nums[3]))
    case = case+1

            
                