arr = [ 1,2,5,7,3,4]
arr.sort()
l = 0
r = len(arr) - 1
k = 8
while (l < r):
    if  (arr[l]+ arr[r]) == k:
        print([arr[l],arr[r]])
        l += 1
        r -= 1
    elif (arr[l]+ arr[r]) > k:
        r -= 1
    else:
        l += 1