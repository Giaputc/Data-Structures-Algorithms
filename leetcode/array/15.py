class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        kq=[]
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum<0:
                    left+=1
                elif sum>0:
                    right-=1
                else:
                    kq.append([nums[left],nums[i],nums[right]])
                    
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return kq
sol = Solution()
print(sol.threeSum([-100,-70,-60,110,120,130,160]))