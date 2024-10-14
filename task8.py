# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7

def PRIME(n):
    mas=[]
    for i in range(2,n+1):
        b=0
        for j in range(2,i):
            if i%j==0:
                b=1
        if b==0: mas.append(i)
    return mas
n=int(input())
mas=PRIME(n)
def raslosh(n):
    if n==1:
        return ''
    else:
        for i in mas:
            if n%i==0:
                return raslosh(int(n/i))+str(i)+'*'
                break
print(raslosh(n)[:-1])
    
