from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter_check=Counter(arr)
        check=list(counter_check.values())
        
        return len(check)==len(set(check))
a = Solution()
print(a)