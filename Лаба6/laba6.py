from math import *
import random as rnd


# Функция
def F(place):
    return - (1 - sin(place[0]) ** 2) * (1 - sin(place[1]) ** 2)

# Основные данные
N = 10 # Число точек
m = 5 # Число роя

# Ограничения
minX = minY = 0
maxX = maxY = 4 * pi
maxV = 0.5

# Изначальные значения
firstPlace = [[rnd.uniform(minX, maxX), rnd.uniform(minY, maxY)] for _ in range(m)]
firstV = [[rnd.uniform(-maxV, maxV), rnd.uniform(-maxV, maxV)] for _ in range(m)]
print('Изначальные значения:')
for i in range(m):
    print(f'{i+1}-е значение:\n [x,y]: [{firstPlace[i][0]}, {firstPlace[i][1]}]\n V[x,y]: [{firstV[i][0]}, {firstV[i][1]}]\n F(x,y): {F(firstPlace[i])}')

# Новые значения
newPlace = firstPlace
newV = firstV

# Лучшее значение точек и функций для каждого
bestPlaceDot = newPlace
bestPlaceValue = [F(bestPlaceDot[i]) for i in range(m)]

# Лучшее значение точек и функций для всех
bestPlaceDotAll = []
bestPlaceValueAll = min(bestPlaceValue)

