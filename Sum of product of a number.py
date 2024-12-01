" Sum of Product of a Given number "

def prod_sum(num):
    prod = 1
    while num > 0:
        rem = num % 10
        prod *= rem
        num = num // 10
    return prod

print(prod_sum(32))
