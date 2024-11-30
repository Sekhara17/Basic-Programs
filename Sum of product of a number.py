n = int(input("Enter number:"))
product_of_number = 1
while n>0:
    remainder = n % 10
    product_of_number *= remainder
    n = n//10
print(product_of_number)
