lis1 = [ 1,2,5,7,3,3,4]
lis1.sort()
left = 0
right = len(lis1)
k = 5
count = 0
while (left < right):
    s = left + right
    if  s == k:
        count += 1
        left += 1
        right -= 1
    if s > k:
        right -= 1
    else:
        left += 1
print("pairs:",count)

