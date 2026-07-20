class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i,x in enumerate(nums):
            if left_sum==(total_sum-left_sum-x):
                return i
            left_sum+=x
        return -1

a = Solution()
print(a.pivotIndex([1,7,3,6,5,6]))