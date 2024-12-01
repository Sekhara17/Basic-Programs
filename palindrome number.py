" PALINDROME NUMNER OR NOT "

class Solution:
    def palin_num(self,num):
        original_number = num
        reversed_number = 0
        while num > 0:
            digit = num % 10
            reversed_number = reversed_number * 10 + digit
            num //= 10

        if original_number == reversed_number:
            return "Yes"
        else:
            return "No"
        
s = Solution()
print(s.palin_num(655))