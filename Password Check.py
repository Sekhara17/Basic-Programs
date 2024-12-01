" PASSWORD CHECKING "

def checkpass(s,min):
    n = len(s)
    cap = 0
    num = 0

    for i in range(len(s)):
        if n < min:
            return 0
        elif s[0].isdigit():
            return 0
        elif s[i] == " " and s[i] == "+":
            return 0
        elif s[i] < "A" and s[i] > "Z":
            return 0
        else:
            return 1
    
s = "B1_&3e5"
min = 4
print(checkpass(s,min))
