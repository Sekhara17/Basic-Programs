def Lists(li1,li2):
    c1 = 0
    c2 = 0
    for i in li1:
        if i not in li2:
            c1 += 1
    for j in li2:
        if j not in li1:
            c2 += 1
    return c1,c2

li1 = [2,3,5,7,9]
li2 = [1,2,3,6,8,9]
print(Lists(li1,li2))