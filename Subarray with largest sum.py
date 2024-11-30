# Given an integer array nums, find the subarray with the largest sum ,and return its sum 

class solution:
    def subarray(self,arr):
        max_sum = float("-inf")
        sum = 0
        for i in range(0,len(arr)):
            sum += arr[i]
            if max_sum < sum:
                max_sum = sum
            if sum < 0:
                sum = 0
        print("Sub array Largest sum:",max_sum)
arr = [-2,1,-3,4,-1,2,1,-5,4]
s = solution()
s.subarray(arr)