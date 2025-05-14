import random as rnd
from math import *

deofantValue = 42
num_rows = 100
num_cols = 4
mutDop = 1  # Величина мутации

# Генерируем случайный массив mas
mas = [[rnd.randint(1, deofantValue) for _ in range(num_cols)] for _ in range(num_rows)]


def deofant(a):
    return a[0] + 3 * a[1] + 5 * a[2] + 7 * a[3]


def takePair(verMas):
    while True:
        vibor1, vibor2 = rnd.random(), rnd.random()
        sum1 = sum2 = 0
        number1 = number2 = 0

        for i, p in enumerate(verMas):
            sum1 += p
            if sum1 >= vibor1:
                number1 = i
                break

        for i, p in enumerate(verMas):
            sum2 += p
            if sum2 >= vibor2:
                number2 = i
                break

        if number1 != number2:
            return number1, number2


def main(mass):
    mas_copy = [row[:] for row in mass]

    # Вычисляем расстояния и вероятности
    distance = [abs(deofant(row) - deofantValue) for row in mas_copy]
    funcPrisp = [1 / d if d != 0 else 0 for d in distance]
    verPrisp = [f / sum(funcPrisp) for f in funcPrisp]

    # Генерируем пары
    pairMas = [takePair(verPrisp) for _ in range(len(distance))]

    # Создаем новый массив
    newMas = [[0] * num_cols for _ in range(num_rows)]

    for i in range(len(newMas)):
        cut = rnd.randint(1, num_cols - 1)  # Точка разреза
        p1, p2 = pairMas[i]

        # Копируем части от двух родителей
        newMas[i][:cut] = mas_copy[p1][:cut]
        newMas[i][cut:] = mas_copy[p2][cut:]

    # Применяем мутацию к строкам с расстоянием выше среднего
    newDistance = [abs(deofant(row) - deofantValue) for row in newMas]
    avg_distance = sum(newDistance) / len(newDistance)

    for i in range(len(newMas)):
        if newDistance[i] > avg_distance:
            for j in range(num_cols):
                # Добавляем случайное значение от -mutDop до mutDop
                mutation = rnd.randint(-mutDop, mutDop)
                newMas[i][j] += mutation
                # Гарантируем, что значения остаются в допустимом диапазоне
                newMas[i][j] = max(1, min(deofantValue, newMas[i][j]))

    # Пересчитываем расстояния после мутации
    newDistance = [abs(deofant(row) - deofantValue) for row in newMas]

    print(f"Среднее расстояние было: {sum(distance) / len(distance)}")
    print(f"Среднее расстояние стало: {sum(newDistance) / len(newDistance)}")

    breakValueItteration = 0
    for i in range(len(newDistance)):
        if newDistance[i] == 0:
            breakValueItteration = 1
            print(f'Решение в строке {i + 1}: {newMas[i]}')

    return newMas, breakValueItteration


print("Изначальный массив (mas):")
for i in range(len(mas)):
    print(f'{i + 1}: {mas[i]}')

breakValue = 0
itteration = 1
while breakValue == 0:
    print(f'\n{itteration} итерация')
    mas, breakValue = main(mas)
    itteration += 1

# print("\nФинальный массив:")
# for i in range(len(mas)):
#     print(f'{i + 1}: {mas[i]}')