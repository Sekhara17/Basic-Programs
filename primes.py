class Solution:
    def primes(self,nums):
        primer= []
        for i in range(2,1000):
            f = 0
            for j in range(2,i):
                if (i % j == 0):
                    f = 1
                    break
            if (f==0):
                primer.append(i)
        prev =0 
        for i in range(len(nums)):
            for p in reversed(primer):
                if (nums[i] > p and nums[i] - p > prev):
                    nums[i] -= p
                    break
            if(nums[i] <= prev):
                return False
            prev = nums[i]
        return True

nums = int(input("enter:"))
s = Solution()
print(primes(nums))