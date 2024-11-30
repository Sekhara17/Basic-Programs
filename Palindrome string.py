def pal(st):
    left = 0
    right = len(st)-1
    while left < right:
           if st[left] == st[right]:   #if st[left]!= st[right]
                 return True            # return False
           left+=1
           right-=1
    return False                         #return True
print(pal("madam"))
