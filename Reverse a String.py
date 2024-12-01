" Optimal and O(n) time complexity "

def rever(str):
    reverse_str=" "
    for char in str:
        reverse_str = char + reverse_str
    return reverse_str
str = "reddi"
print(rever(str))

" Little bit more time complexity "

def revers(str):
    reverse_str=" "
    for char in range(len(str)):
        if str != str[::-1]:
            reverse_str += str[char]
    s = reverse_str[::-1]
    return s
print(revers("reddi"))