class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_curr=max(candies)
        path=[]
        for c in candies:
            if c+extraCandies>max_curr:
                path.append(True)
            else:
                path.append(False)
        return path