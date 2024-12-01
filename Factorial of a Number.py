" FACTORIAL OF A NUMBER "

def fact(num):
    res = 1
    for i in range(num,1,-1):
        res *= i
        i += 1
    return res

print(fact(5))