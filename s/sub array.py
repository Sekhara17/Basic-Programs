def maxarray(s):
    l = [""]
    max = -100000
    for i in range(len(s)):
        s += l 
        if (s>max):
            max = s
        if (s<0):
            s = 0
    return max
s = [ 15,3,7,7,8]
print(maxarray(s))