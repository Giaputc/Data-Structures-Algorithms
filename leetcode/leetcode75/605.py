class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n<=0:
            return True
        len1 = len(flowerbed)
        for i in range(len1):
            if flowerbed[i]==0:
                if i==0:
                    oke_trai=True
                else:
                    oke_trai=(flowerbed[i-1]==0)
                if i==len1-1:
                    oke_phai=True
                else:
                    oke_phai=(flowerbed[i+1]==0)
                if oke_phai and oke_trai:
                    flowerbed[i]=1
                    n-=1
        return n<=0