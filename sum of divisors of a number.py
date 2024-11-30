number = input("Enter number:")
divisor = []
for i in range(1,number):
    if i%number==0:
        divisor+=int(i)
    print(divisor)