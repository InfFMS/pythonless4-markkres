# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3
M,N=map(int,input().split())
def PRIME(n):
    mas=[]
    for i in range(2,n+1):
        b=0
        for j in range(2,i):
            if i%j==0:
                b=1
        if b==0: mas.append(i)
    return mas
mas=PRIME(max(N,M))
def raslosh(n):
    if n==1:
        return ''
    else:
        for i in mas:
            if n%i==0:
                return raslosh(int(n/i))+str(i)
                break
k=raslosh(max(N,M))
for i in range(len(k)):
    if N%int(k[i])==0 and M%int(k[i])==0:
        N,M=int(N/int(k[i])),int(M/int(k[i]))
print(N,M)
