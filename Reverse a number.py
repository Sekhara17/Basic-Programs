" REVERSE A GIVEN NUMBER "

class solution:
    def reverse_num(self,num):
        rev_num = 0
        while num > 0:
            rem = num % 10
            rev_num = rev_num * 10 + rem
            num = num // 10
        return rev_num

s = solution()
print(s.reverse_num(1234))
