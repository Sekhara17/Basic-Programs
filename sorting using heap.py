import heapq
def heaps(arr):
    heapq.heapify(arr)
    return arr
arr = [3,2,1,5]
print(heaps(arr))



class Solution:
    def kthSmallest(self,arr,k):
        heapq.heapify(arr)
        res =- 1
        while (k>0):
            res = heapq.heappop(arr)
            k -= 1
        return res
arr = [2,4,3,1]
s = Solution()
print(s.kthSmallest(arr,k))