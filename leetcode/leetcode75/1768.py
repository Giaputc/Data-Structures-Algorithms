class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        n1,n2=len(word1),len(word2)
        for i in range(max(n1,n2)):
            if i<n1:
                res.append(word1[i])
            if i<n2:
                res.append(word2[i])
        return "".join(res)
s=Solution()
print(f"{s.mergeAlternately('abc','12345')}")