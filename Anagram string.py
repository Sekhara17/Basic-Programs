def anagram_str(str1,str2):
    if len(str1) != len(str2):
        return "No"
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    return "Yes" if sorted_str1 == sorted_str2 else "No"
str1 = "sekhar"
str2 = "skhrae"
print(anagram_str(str1,str2))