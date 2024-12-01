" LARGEST NUMBER IN AN ARRAY "

class Solution:
    def largest_num(self,arr):
        max1 = arr[0]
        for i in range(len(arr)):
            if arr[i] > max1:
                max1 = arr[i]
        return max1

s = Solution()
print(s.largest_num([1,9,11,10]))
