" SWAPPING THREE NUMBERS "

def swap_num(f_num,s_num,t_num):
    temp = f_num
    f_num = s_num
    s_num =  t_num
    t_num = temp
    return f_num,s_num,t_num

print(swap_num(3,4,6))