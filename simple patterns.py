def num(n):
    for i in range(1,n):
        for j in range(1,n):
            # print(i,end = " ") 
            # print(j,end = " ")   
            # print("*",end = " ") 
            # print(i%2,end = " ")
             print(j%2,end = " ")  
        print()
num(5)


def num(m):
    for i in range(m,0,-1):
        for j in range(m,0,-1):
            #print(i,end=" ")
            #print(j ,end=" ")
            print("*",end = " ")
        print()
num(5)


