class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # nums_zero=0
        # left=0
        # max_leng=0
        # for right in range(len(nums)):
        #     if nums[right]==0:
        #         nums_zero+=1
        #     while nums_zero>1:
        #         if nums[left]==0:
        #             nums_zero-=1
        #         left+=1
        #     max_leng=max(max_leng,right-left)
        # return max_leng
        
        left, most = 0, 1
        for x in nums:
            if x == 0:
                most -= 1
            if most < 0:
                if nums[left] == 0:
                    most += 1
                left += 1
        return len(nums) - left - 1
#hạn chế dùng max,cùng 1 thuật toán O(N) nhưng cách 2 có tối ưu hơn nhiều
a=Solution()
print(a.longestSubarray([1,1,0,1]))
