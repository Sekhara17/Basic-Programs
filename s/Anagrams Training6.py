s1 = "catb"
s2 = "tacb"
f  = 0
for i in s1:
    if i not in s2:
        f = 1
        break
if (f == 0):
    print("Anagrams")
elif (f==1 or len(s1) != len(s2)):
    print("Not Anagrams")