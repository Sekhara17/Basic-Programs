def sap(w1,w2):
    w11 = ""
    w12 = ""
    for i in range(len(w1)):
        if w1 != w2:
            w11 += w1[i]
            w12 += w2[i]
        if w11 == w12:
            return True
    return False
w1 = ["ab","c"]
w2 = ["a","bc"]
print(sap(w1,w2))

