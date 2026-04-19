class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


s="Pham Van Giap"
print(s.split()[::-1])