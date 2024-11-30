def rever(str):
    words = str.split()
    reverse_word = words[::-1]
    reverse_sentence = ' '.join(reverse_word)
    return reverse_sentence
str = "hello world!"
print(rever(str))