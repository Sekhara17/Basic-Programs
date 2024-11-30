def fibo(n):
    if n<= 1:
        return n
    return fibo(n-1)+fibo(n-2)
n = 4
print(fibo(n))