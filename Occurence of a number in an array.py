" OCCURENCE OF A PARTICULAR NUMBER IN AN ARRAY "

class Solution:
    def occur_num(self,arr):
        element =2
        n =len(arr)
        count =0
        for i in range(0,n):
            if arr[i]==element:
                count+=1
        return " Occurence of 2 :",count

s = Solution()
print(s.occur_num([1,2,4,5,3,2,2]))