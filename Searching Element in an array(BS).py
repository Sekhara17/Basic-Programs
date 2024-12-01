" BINARY SEARCH "

class solution:
    def bs(self,arr,target):
        low = 0
        mid = 0
        high = len(arr)-1
        while low<=high:
            mid  = (low +high)//2
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid]> target:
                high = mid -1
            else:
                return mid
        return -1
arr = [1,4,5,16,19,20]
target =16
s = solution()
res = s.bs(arr,target)
if res != -1:
    print("Index of target:",res)
else:
    print("not found")         