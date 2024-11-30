def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def prime_numbers_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

primes = prime_numbers_in_range(start, end)

if primes:
    print(f"Prime numbers between {start} and {end} are: {primes}")
else:
    print(f"There are no prime numbers between {start} and {end}.")