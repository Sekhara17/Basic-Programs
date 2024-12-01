" 1. REVERSE A GIVEN NUMBER "

def rev_num(num):
    rev_num = 0
    while num != 0:
        temp = num % 10
        rev_num = rev_num * 10 + temp
        num = num // 10
    return rev_num
#print(rev_num(12345))


" 2. COUNT NO OF CHARACTERS IN A GIVEN STRING "

def char_count(str1):
    count = 0
    for char in range(len(str1)):
        if str1[char] == " ":
            char += 1
        else:
            count += 1
    return count
#print(char_count("Accenture coding round"))

" 3. FIND A MISSING NUMBER "

def mis_num(arr):
    n = len(arr)
    total = n * (n + 1) // 2
    sum1 = 0
    for i in range(n):
        sum1 += arr[i]

    return total - sum1
#print(mis_num([0,3,4,1]))

" 4. RETURN 1 TO M RANGE ELEMENTS SUM DIFFERENCE , WHICH ARE DIV BY N - WHICH ARE NOT DIV BY N"

def diff_sum(n,m):
    n_div_sum1 = 0
    n_not_div_sum2 = 0
    for i in range(1,m+1):
        if i % n == 0:
            n_div_sum1 += i
        else:
            n_not_div_sum2 += i
    return abs(n_div_sum1 - n_not_div_sum2)
#print(diff_sum(4,20))

" 5. FIBONACCI SERIES "

def fibo(num):
  if num<=1:
        return num
  return fibo(num-1)+fibo(num-2)
#print(fibo(4))

" 6. PRIME NUMBER OR NOT "

def prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
#print(prime(11))

" 7. SUM OF ODD & EVEN INDEX ELEMENTS "

def sum_even_odd(arr):
    n = len(arr)
    even_sum = 0
    odd_sum = 0
    for i in range(n):
        if arr[i] % 2 == 0:
            even_sum += arr[i]
        else:
            odd_sum += arr[i]
    return even_sum,odd_sum
#print(sum_even_odd([1,2,3,4,5,6]))

" 8. RETURN LENGTH OF THE LAST WORD IN A GIVEN STRING "

def len_word(str1):
    n = len(str1)
    word_len = 0
    for i in range(n):
        if str1[i] == " ":
            word_len = 0
        else:
            word_len += 1
    return word_len      
#print(len_word("hello words"))

" 9. RETURN  MAX SUBARRAY  SUM "

def max_subarray(arr):
    sum1 = 0
    max1 = 0
    for i in range(len(arr)):
        sum1 += arr[i]
        max1 = max(max1,sum1)
        if sum1 < 0:
            sum1 = 0
    return max1
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))