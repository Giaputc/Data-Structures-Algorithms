nums=[1,1,1,0,0,0,1,1,1,1,0]
k=2
dem0=0
left=0
max_0=0
for right in range(len(nums)):
    if nums[right]==0:
        dem0+=1
    while dem0>k:
        if nums[left]==0:
            dem0-=1
        left+=1
    max_0=max(max_0,right-left +1)

print(max_0)