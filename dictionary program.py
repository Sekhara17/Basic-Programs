num = 13
s = set()
res = 0
for k in range((num//2)+1,0,-1):
    if num//k not in s:
        res += num//k
        s.add(num//k)
print(res)    