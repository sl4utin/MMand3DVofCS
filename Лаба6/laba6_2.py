from math import *
import random as rnd


# Функция для вычисления значения
def F(place):
    return -(1 + sin(place[0]) ** 2) * (1 + sin(place[1]) ** 2)


# Основные параметры
N = 10  # Количество итераций
m = 5  # Количество частиц в рое

# Границы поиска
minX = minY = 0
maxX = maxY = 4 * pi
maxV = 0.5  # Максимальная скорость

# Инициализация начальных позиций и скоростей
place = [[rnd.uniform(minX, maxX), rnd.uniform(minY, maxY)] for _ in range(m)]
speed = [[rnd.uniform(-maxV, maxV), rnd.uniform(-maxV, maxV)] for _ in range(m)]

# Вывод начальных значений
print('Изначальные значения:')
for i in range(m):
    print(f'{i + 1}-я частица:')
    print(f'  Позиция: [x={place[i][0]:.3f}, y={place[i][1]:.3f}]')
    print(f'  Скорость: [vx={speed[i][0]:.3f}, vy={speed[i][1]:.3f}]')
    print(f'  Значение F: {F(place[i]):.3f}\n')

# Инициализация лучших значений
best_local_places = place.copy()  # Лучшие позиции для каждой частицы
best_local_values = [F(p) for p in place]  # Лучшие значения для каждой частицы

# Находим глобальный лучший результат
best_global_value = min(best_local_values)
best_global_index = best_local_values.index(best_global_value)
best_global_place = best_local_places[best_global_index]

print('Начальные лучшие значения:')
print(f'Глобальный лучший: F={best_global_value:.3f} при [x={best_global_place[0]:.3f}, y={best_global_place[1]:.3f}]')

# Основной цикл алгоритма
for iteration in range(N):
    print(f'\n--- Итерация {iteration + 1} ---')

    # Обновляем позиции частиц (упрощенная версия)
    for i in range(m):
        # Простое случайное движение (в реальном PSO здесь сложная логика)
        new_x = place[i][0] + speed[i][0]
        new_y = place[i][1] + speed[i][1]

        # Проверка границ
        new_x = max(minX, min(new_x, maxX))
        new_y = max(minY, min(new_y, maxY))

        place[i] = [new_x, new_y]

        # Вычисляем новое значение функции
        current_value = F(place[i])

        # Обновляем лучшие значения для частицы
        if current_value < best_local_values[i]:
            best_local_values[i] = current_value
            best_local_places[i] = place[i].copy()

            # Проверяем на глобальный лучший
            if current_value < best_global_value:
                best_global_value = current_value
                best_global_place = place[i].copy()

        # Изменение скорости
        alpha = rnd.random()
        beta = 1 - alpha
        for nv in range(m):
            speed[nv][0] += alpha * (best_local_places[nv][0] - place[nv][0]) + beta * (best_global_place[0] - place[nv][0])
            speed[nv][0] = max(-maxV, speed[nv][0])
            speed[nv][0] = min(maxV, speed[nv][0])

            speed[nv][1] += alpha * (best_local_places[nv][1] - place[nv][1]) + beta * (best_global_place[1] - place[nv][1])
            speed[nv][1] = max(-maxV, speed[nv][1])
            speed[nv][1] = min(maxV, speed[nv][1])


    # Вывод информации о текущем состоянии
    print('\nТекущие позиции:')
    for i in range(m):
        print(f'Частица {i + 1}: [x={place[i][0]:.3f}, y={place[i][1]:.3f}] F={F(place[i]):.3f}, [Vx={speed[i][0]:.3f}, Vy={speed[i][1]:.3f}]')

    print('\nЛучшие локальные значения:')
    for i in range(m):
        print(
            f'Частица {i + 1}: F={best_local_values[i]:.3f} при [x={best_local_places[i][0]:.3f}, y={best_local_places[i][1]:.3f}]')

    print(
        f'\nГлобальный лучший: F={best_global_value:.3f} при [x={best_global_place[0]:.3f}, y={best_global_place[1]:.3f}]')

# Финальный вывод
print('\nФинальные результаты:')
print(f'Лучшее найденное решение: F={best_global_value:.3f}')
print(f'При координатах: [x={best_global_place[0]:.3f}, y={best_global_place[1]:.3f}]')