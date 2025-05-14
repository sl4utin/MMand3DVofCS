import random as rnd
from math import *

def rangFind():
    rang = [0] * len(fitnes)
    for i in range(len(fitnes)):
        for j in range(len(fitnes)):
            if (fitnes[j] <= fitnes[i]):
                rang[i] += 1
    return rang

def rulet():
    mas = [0] * 14
    for n in range(len(mas)):
        vibor = rnd.random()
        sum = 0
        number = 0
        while sum < vibor:
            sum += fitnesVer[number]
            number += 1
        mas[n] = number
    return mas


def stah():
    mas = [0] * 14
    vibor = rnd.random()
    for n in range(len(mas)):
        sum = 0
        number = 0
        while sum < vibor:
            sum += fitnesVer[number]
            number += 1
        mas[n] = number
        vibor+=1/len(mas)
        if(vibor >= 1): vibor -= 1
    return mas


def rang():
    mas = [0] * len(fitnes)
    for n in range(len(mas)):
        vibor = rnd.random()
        summa = 0
        number = 0
        while summa < vibor:
            summa += fitnesRangVer[number]
            number += 1
        mas[n] = number
    return mas


def usechenie():
    l = 0.4
    count = ceil(len(fitnes) * l)
    mas = [0] * count
    for n in range(count):
        number = 0
        while ((len(fitnes) - n) != fitnesRang[number]):
            number += 1
        mas[n] = number + 1
    return mas


def turnir_binar():
    count = 10
    mas = [0] * count
    for n in range(count):
        first = rnd.randint(1, len(fitnes))
        second = rnd.randint(1, len(fitnes))
        while(first == second):
            second = rnd.randint(1, len(fitnes))
        if(fitnes[first - 1] > fitnes[second - 1]):
            mas[n] = first
        else:
            mas[n] = second
    return mas


#         1    2    3    4    5    6    7    8     9    10   11   12   13   14
fitnes = [4.0, 3.3, 9.0, 5.0, 2.0, 8.0, 2.1, 12.0, 7.1, 4.6, 5.8, 9.1, 1.3, 8.2]

# Для 1 и 2
fitnesVer = [fitnes[i] / sum(fitnes) for i in range(len(fitnes))]

# Для 3
fitnesRang = rangFind()
fitnesRangVer = [fitnesRang[i] / sum(fitnesRang) for i in range(len(fitnesRang))]

print('\nВероятность фитнес от общей суммы')
print(fitnesVer)

print('\nРулетка')
print(rulet())
#[1, 4, 8, 8, 5, 7, 14, 4, 8, 14, 3, 4, 12, 9]

print('\nСтахастическая универсальная')
print(stah())
#[2, 3, 3, 5, 6, 8, 8, 8, 9, 10, 11, 12, 14, 14]

print('\nРанжированная селекция')
print('Ранги:')
print(fitnesRang)
print('Выбор:')
print(rang())


print('\nСелекция усечения')
print(usechenie())


print('\nТурнирный отбор (бинарный)')
print(turnir_binar())
