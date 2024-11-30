
def occur(st):
    st1 = ""
    for i in range(len(st)):
        if st[i]== "a":
            st1 += "b"
        elif st[i]=="b":
            st1 += "a"
        elif st[i] != "a" or "b":
            st1 += st[i]
    print(st1)
st = "abaabbccdghm"
occur(st)
