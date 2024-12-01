def subarray(arr):
    n = len(arr)
    left = 0
    right = n - 1
    count = 0
    for i in range(n):
        if left < right:
            left += 1
            right -= 1
        elif left >= right:
            count += 1
            right -= 1
    return count
arr = [1,2,3,2,2,3,5]
print(subarray(arr))