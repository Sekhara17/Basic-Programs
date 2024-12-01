" FIND PRIPLETS IN AN ARRAY "

class Solution:
    def prips(self,n):
        sum = 4
        count = 0
        for i in range(len(n)-2):
            for j in range(i+1,len(n)-1):
                for k in range(j+1,len(n)):
                    if n[i]+n[j]+n[k] == sum:
                        count+=1
                        print(n[i],n[j],n[k])
        if count == 0:
            return " Priplets not found "
        return count

s = Solution()
print(s.prips([0,0,1,2,3,4,5]))