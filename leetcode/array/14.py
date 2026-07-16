strs=["flower","flow","flight"]

strs.sort()#$ O(N.logN.M)

first = strs[0]
last = strs[-1]

i = 0

while i < len(first) and i < len(last) and first[i] == last[i]:#O(M)
    i += 1

print(first[:i])

#
# ý tưởng: sort chuỗi,và chỉ cần so sánh 2 chuỗi đầu và cuối giống nhau
# vậy tại sao không cần so sánh chuỗi ở giữa.vì ở chữ ở giữa sé nằm trong khoảng 
#  lớn hơn chuỗi đầu và nhỏ hoặc bằng chuỗi cuối#