arr  = [1,4,5,6,7,3,2]
max_sum = 0
s = 0
for i in arr:
    s += i
    if max_sum > s:
        max_sum = s
    if s < 0:
        s = 0
print(max_sum)