class Solution:
    def reverseVowels(self, s: str) -> str:
        chuoi=list(s)
        vowels=set("aeiouAEIOU")
        trai,phai=0,len(chuoi)-1
        while trai<phai:
            if chuoi[trai] not in vowels:
                trai+=1
            elif chuoi[phai] not in vowels:
                phai-=1
            else:
                chuoi[trai],chuoi[phai]=chuoi[phai],chuoi[trai]
                trai+=1
                phai-=1
        return "".join(chuoi)