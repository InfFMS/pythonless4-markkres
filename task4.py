# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.

def nod(a,b):
    if b==0:
        return a
    else:
        return nod(b,a%b)
a = int(input())
b = int(input())
print(nod(a,b))
