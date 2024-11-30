def and_op(s1,s2):
    res = " "
    for i in range(len(s1)):
        if s1[i] == "1" and s2[i] =="1":
            res+="1"
        else:
            res+="0"
    return res
print(and_op("1101","0011"))

def or_op(s1,s2):
    res = " "
    for i in range(len(s1)):
        if s1[i] == "1" or s2[i] =="1":
            res+="1"
        else:
            res+="0"
    return res
print(or_op("1101","0011"))

def xor_op(s1,s2):
    res = " "
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            res+="0"
        else:
            res+="1"
    return res
print((xor_op("1101","0011")))




