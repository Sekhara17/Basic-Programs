arr = [ 1,3,6,4,2,7]
sum = 5
l_sum = 0
arr.sort()
if arr[0] + arr[1] < sum :
        l_sum += arr[0] * arr[1]
print(l_sum)
