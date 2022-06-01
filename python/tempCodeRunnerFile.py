if nums[0]+nums[1]+nums[2]+nums[3]==1000000:
        print("Case #"+str(case)+": "+ str(nums[0]) +" "+str(nums[1]))+" "+str(nums[2])+" "+str(nums[3])
    elif nums[0]+nums[1]+nums[2]+nums[3] <1000000:
        print("Case #"+str(case)+": IMPOSSIBLE")
    
    elif nums[0]+nums[1]+nums[2]+nums[3] >1000000:
        while(nums[0]+nums[1]+nums[2]+nums[3]!=1000000):
            if(snums[-1]>=nums[0]+nums[1]+nums[2]+nums[3]-1000000):
                snums[-1] = snums[-1] - (nums[0]+nums[1]+nums[2]+nums[3]-1000000)      
            elif(snums[-1]+snums[-2] >= (nums[0]+nums[1]+nums[2]+nums[3]-1000000)):
                snums[-2] = (nums[0]+nums[1]+nums[2]+nums[3]-1000000) - snums[-1]
                snums[-1] =0

            elif(snums[-1]+snums[-2]+snums[-3] >= (nums[0]+nums[1]+nums[2]+nums[3]-1000000)):
                snums[-3] = (nums[0]+nums[1]+nums[2]+nums[3]-1000000) - snums[-1] - snums[-2]
                snums[-1] =0
                snums[-2] =0

            elif(snums[-1]+snums[-2]+snums[-3]+snums[-4] >= (nums[0]+nums[1]+nums[2]+nums[3]-1000000)):
                snums[-4] = (nums[0]+nums[1]+nums[2]+nums[3]-1000000) - snums[-3] - snums[-2] -snums[-1]
                snums[-1] =0
                snums[-2] =0
                snums[-3] =0

            print("Case #"+str(case)+": "+ str(snums[0]) +" "+str(snums[1]))+" "+str(snums[2])+" "+str(snums[3])

            