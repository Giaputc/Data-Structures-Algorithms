class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1=set(nums1)
        set2=set(nums2)
        
        check1=list(set1-set2)
        check2=list(set2-set1)
        
        return [check1,check2]
a = Solution()
print(a.findDifference([1,2,3],[2,4,6]))