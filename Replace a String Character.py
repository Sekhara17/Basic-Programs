"REPLACE A CHARACTER IN A GIVEN STRING "

def str_char(str,ch1,ch2):
    res_str=" "
    for char in range(len(str)):
        if char == ch1:
            res_str += ch2
        elif char == ch2:
            res_str += ch1
        else:
            res_str += char
    return res_str
str= "apples"
ch1="a"
ch2 ="p"
print(str_char(str,ch1,ch2))
