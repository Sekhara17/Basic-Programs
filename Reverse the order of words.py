def strr(s):
    ans = []
    temp = ""
    for c in s:
        if c != " ":
            temp += c
        elif temp !="":
            ans.append(temp)
    return temp

s = "hello world"
print(strr(s))