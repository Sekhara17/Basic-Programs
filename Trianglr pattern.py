def  pascal(g):
    for i in range(g+1):
        for j in range(i):
            print("*",end=" ")
        print()
pascal(4)

print("PASCAL RIGHT \nPASCAL LEFT ")


def revPascal(n):
    for i in range(n):
        for j in range(i,n):
            print("*",end=" ")
        print()
revPascal(4)