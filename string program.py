# input str = "string"
# output  str = "rtsng"


s = "string"
n = len(s)
s1 = ""
for i in range(n):
    if s[i] == "i" or s[i] == "I":
        break
    else:
        s1 = s1+s[i]

s1 = s1[::-1]
for j in range(i+1,n):
    s1 = s1 + s[j]
print(s1)
