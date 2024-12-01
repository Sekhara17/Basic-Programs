" THREE NUMBERS SUM EQUAL TO ZERO PAIRS "

class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum_ < 0:
                    left += 1
                else:
                    right -= 1
        return result
nums = [-1,0,1,2,-1,-4]
s = Solution()
res=s.threeSum(nums)
print(res)