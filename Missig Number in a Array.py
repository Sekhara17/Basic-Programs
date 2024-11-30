class solution:
    def missing(self,nums):
        n = len(nums)
        sum1 = 0
        for i in range(0,n):
            sum2 = n*(n+1)//2
            sum1+=nums[i]
        return sum2-sum1
nums = [0,3,1,5,2]
s = solution()
res = s.missing(nums)
print("Missing number:",res)

#arr = [1,2,4,5,6]
#n =len(arr)
#sum1= n *(n+1)//2
#sum2 =sum(arr)
#sum3 = sum2-#sum1
#print("Missi#ng number:",sum3##)