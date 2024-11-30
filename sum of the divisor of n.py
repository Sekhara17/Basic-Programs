def sum_of_divisor(num):
    sum_of_divisor_num = 0
    for i in range(1,num+1):
        if num % i==0:
            sum_of_divisor_num += i
    return sum_of_divisor_num
num = 12
print(sum_of_divisor(num))