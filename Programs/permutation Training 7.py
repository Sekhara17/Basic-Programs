s1 = "awrtiou"
vowel = "aeiouAEIOU"
count = 0
for i in s1:
    if i in vowel:
        count += 1
f = 1
n = len(s1) - count
for i in range(1,n+1):
    f = f * i      
print(f)