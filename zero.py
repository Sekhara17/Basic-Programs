def arranging_zero(num):
    n = len(num)
    temp = []
    left = 0
    for i in range(n):
        if num[i]==0:
            temp = num[i]
        else:
            temp = num[i]
            num[i]=left
    return temp
num = [0,2,0,6,0,0,7]
print(arranging_zero(num))

