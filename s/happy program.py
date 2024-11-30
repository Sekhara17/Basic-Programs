def happy(n):
    def sum_squares(k):
        total = 0
        while k > 0:
            digit = k % 10
            total += digit * digit
            k //= 10
        return total
    s = set()
    while n != 1 and n not in s:
        s.add(n)
        n = sum_squares(n)
    return n == 1
n = int(input())
print(happy(n)) 