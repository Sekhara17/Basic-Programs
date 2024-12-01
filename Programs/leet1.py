class Solution:
    def maximumBeauty(self, items,queries):
        items.sort()
        res = []
        bty = [0] * len(items)
        bty[0] = items[0][1]
        for i in range(1,len(items)):
            bty[i] = max(bty[i-1],items[i][1])
        for qry in queries:
            i = 0
            j = len(items)-1
            b = 0
            while i <= j:
                m = (i + j) // 2
                if items[m][0] <= qry:
                    b = bty[m]
                    i = m+1
                else:
                    j = m - 1
            res.append(b)
        return res
items = []
queries = []
s = Solution()
print(s.maximumBeauty(items,queries))