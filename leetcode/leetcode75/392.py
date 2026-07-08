class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        p = -1
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i]==t[j] and j > p:
                    p = j
                    k = k + 1
                    break
        if k == len(s):
            return True
        else:
            return False

