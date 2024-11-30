def palim(s1):
    n = len(s1)
    left = 0
    right = n - 1
    for i in range(n):
        if s1[left] <= s1[right]:
            left += 1
            right -= 1
        else:
            return False   
    return True

s1 = input()
print(palim(s1))