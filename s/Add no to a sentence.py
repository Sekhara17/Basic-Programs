def sente(word):
    if len(word) > 10:
        return word[0] + str(len(word) - 2) + word[-1]
    return word
def sent(sentence):
    words = sentence.split()
    return ' '.join([sente(word) for word in words])

sentence = "I am very happy to introducing you to my girlfriends"
print(sent(sentence))
