lis1  = [2,7,11,15]
target = 9
ans = [ ] * 2
dict1 = {}

for i in range(len(lis1)):
    if target - lis1[i] not in dict1:
        dict1.append(lis1)
    else:

        ans += 1
print(dict1)
