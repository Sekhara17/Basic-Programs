def occurence(s):
    s1 = set(s)
    for a in s1:
        print(a,s.count(a),sep =" --> ")

s = [10,15,10,5,15,10]
occurence(s)