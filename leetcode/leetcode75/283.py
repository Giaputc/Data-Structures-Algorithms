#nums = [0, 1, 0, 3, 12]
nums=[1]
last_none_zero=0
for i in range(0,len(nums),1):
    tmp=nums[last_none_zero]
    if nums[i]!=0:
        nums[last_none_zero]=nums[i]
        nums[i]=tmp
        last_none_zero+=1
print(nums)