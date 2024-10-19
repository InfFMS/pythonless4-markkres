# Напишите функцию convert_base(num, from_base, to_base),
# которая переводит натуральное число num из системы
# счисления с основанием from_base в систему счисления
# с основанием to_base
# 2 ≤ to_base ≤ 36 ; 2 ≤ from_base ≤ 36
# На входе три числа num, from_base, to_base
# На выходе одно число - результат работы функции
# Подсказка (если не получается решить):
# Попробуйте разбить задачу на две подзадачи:
# перевод из десятичной системы счисления в любую
# перевод из любой системы счисления в десятичную
# Объедините эти две подзадачи, получите ответ.
def convert_base(num, from_base, to_base):
    dec=int(str(num), from_base)
    if to_base==10:
        return dec
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res=''
    while dec>0:
        res=digits[dec%to_base]+res
        dec=dec//to_base
    return res
print(convert_base(15,8,10))
