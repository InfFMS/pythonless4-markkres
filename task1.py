# Напишите процедуру, которая принимает параметр – натуральное число N –
# и выводит на экран треугольник из * с катетами равными N.
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
def f(n):
    for i in range(n):
        for j in range(i+1): print("*",end='')
        print()
print(f(int(input())))
