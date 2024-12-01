" MISSING NUMBER IN AN ARRAY "

class Solution:
    def mis_num(self,nums):
        n = len(nums)
        sum1 = 0
        for i in range(0,n):
            sum2 = n * (n+1) // 2
            sum1 += nums[i]
        return sum2 - sum1

s = Solution()
print(s.mis_num([0,3,1,5,2]))