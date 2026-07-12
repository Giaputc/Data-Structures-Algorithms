s = "abciiidef"
k = 3
check=set("aeiou")
dem=0
for i in range(k):
    if s[i] in check:
        dem+=1
max_dem=dem
for i in range(k,len(s)):
    if s[i] in check:
        dem+=1
    if s[i-k] in check:
        dem-=1
    if dem>max_dem:
        max_dem=dem

print(max_dem)