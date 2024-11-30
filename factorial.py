def fact(n):
    result = 1
    for i in range(n,1,-1):
        result*=i
        i+=1
    return result
n = 5
print(fact(n))