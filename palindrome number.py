#User function Template for python3

class Solution:
    def is_palindrome(self,x):
        
        original_number = x
        reversed_number = 0
        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x //= 10

        if original_number == reversed_number:
            return "Yes"
        else:
            return "No"
c = Solution()
print(c.is_palindrome(555))