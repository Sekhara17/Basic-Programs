import math
def sum_of_square_roots(m, n):
    sum_even_sqrt = 0
    sum_odd_sqrt = 0
    
    for i in range(m, n + 1):
        sqrt_val = math.sqrt(i)
        if i % 2 == 0:
            sum_even_sqrt += sqrt_val
        else:
            sum_odd_sqrt += sqrt_val
    
    return sum_even_sqrt, sum_odd_sqrt

# Example usage
m = 1
n = 10
even_sqrt_sum, odd_sqrt_sum = sum_of_square_roots(m, n)
print(f"Sum of square roots of even numbers: {even_sqrt_sum}")
print(f"Sum of square roots of odd numbers: {odd_sqrt_sum}")