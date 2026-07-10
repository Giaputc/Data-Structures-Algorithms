#co the dung hashmap

#two points
nums=[3,1,3,4,3]
k=6
nums.sort()
l,r=0,len(nums)-1
ope=0
while l<r:
    sum=nums[l]+nums[r]
    if sum==k:
        ope+=1
        l+=1
        r-=1
    elif sum<k:
        l+=1
    elif sum>k:
        r-=1
print(ope)