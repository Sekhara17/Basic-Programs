lis = [1,2,6,5,4,3]

lis.sort()
even_list  = []
odd_list  = []
for i in range(0,len(lis)):
    if lis[i] % 2 ==0:
        even_list.append(lis[i])
    else:
        odd_list.append(lis[i])
print(odd_list[1] + even_list[len(even_list) - 2])