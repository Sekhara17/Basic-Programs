class Solution:
    def basic(number):
        n = len(number)
        num_list = []
        for num in range(n):
            if num%2==0:
                num_list.append(num)
        return num_list
number = [1,2,4,3,5,6]
s = Solution()
print(s.basic(number))