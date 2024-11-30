class solution:
    def largest(self,arr):
        max = arr[0]
        for i in range(len(arr)):
            if arr[i]>max:
                max = arr[i]
        print("Largest number in the array:",max)
arr = [1,9,11,10]
s = solution()
s.largest(arr)
