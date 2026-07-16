class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_all=0
        curr_all=0
        for g in gain:
            curr_all+=g
            if curr_all>max_all:
                max_all=curr_all
        return max_all
        
a=Solution()
print(a.largestAltitude([-5,1,5,0,-7]))