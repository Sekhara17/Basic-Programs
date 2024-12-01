" PALINDROME STRING OR NOT "

def palin(str1):
    left = 0
    right = len(str1)-1
    while left < right:
        if str1[left] == str1[right]:   #if str1[left]!= str1[right]
            return True            # return False
        left+=1
        right-=1
    return False                         #return True
print(palin("madam"))
