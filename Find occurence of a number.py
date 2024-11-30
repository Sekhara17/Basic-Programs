#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		coun_dup = 0
		for i in arr:
			if i == x:
				coun_dup+=1
		return coun_dup
arr = [1,1,2,2,2,2,3]
n =7
x = 2
s = Solution()
print(s.count(arr,n,x))