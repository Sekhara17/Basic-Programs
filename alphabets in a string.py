#User function Template for python3

class Solution:

    def Count(self, S):
        count = 0
        for i in range(len(S)):
            if S[i].isalpha():
                count+=1
        return count
S ="7$!bc#$02"
s = Solution()
res =s.Count(S)
print(res)