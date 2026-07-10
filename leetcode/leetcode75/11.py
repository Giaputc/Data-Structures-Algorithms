height=[1,8,6,2,5,4,8,3,7]
res=0
l,r=0,len(height)-1
abs=max(height)
while l< r:
    ares=(r-l)*min(height[l],height[r])
    res=max(res,ares)
    if height[l]<height[r]:
        l+=1
    else:
        r-=1
    if res>abs*(r-l):
        break
print(res)