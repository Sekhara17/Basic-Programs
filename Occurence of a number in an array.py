class solution:
    def occur(self,arr):
        element =2
        n =len(arr)
        count =0
        for i in range(0,n):
            if arr[i]==element:
                count+=1
        print("occurence of 2 is:",count)

arr = [1,2,4,5,3,2,2]
s = solution()
s.occur(arr)