class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        clost=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                current = nums[i] + nums[left] + nums[right]
                if current==target:
                    return current
                if abs(target-current)<abs(target-clost):
                    clost=current
                if current<target:
                    left+=1
                else:
                    right-=1
        return clost
a = Solution()
print(a.threeSumClosest([-1,2,1,-4],1))