class solution:
    def paln(self,num):
        reversed_num = 0
        while num>0:
            remainder = num % 10
            reversed_num = reversed_num * 10 + remainder
            num = num//10
        print("After Reversing :",reversed_num)
num = 1234
n = solution()
n.paln(num)
