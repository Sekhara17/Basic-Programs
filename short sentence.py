" SHORT THE WORD IN A SENTENCE IF A WORD CONTAINS MORE THAN 10 CHARACTERS AS WELL AS SENTENCE "

def short_word(n):
    if len(n)>10:
        return n[0]+ str(len(n)-2)+n[-1]
    return n

def short_sentence(n1):
    n3 = n1.split()
    return ' '.join([short_word(n) for n in n3])

n = "sekharreddy"
print(short_word(n))
n1 = "sekhar is reddisekahra"
print(short_sentence(n1))
