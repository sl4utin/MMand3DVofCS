from math import exp
from random import randint, random

w_values = [4, 6, 2, 8, 9, 1, 3, 5, 4, 3]
c_values = [5.0, 4.5, 6.0, 4.0, 3.5, 7.0, 4.0, 3.0, 6.5, 5.5]
MAX_WEIGHT = 32

def evaluate(x_values):
    total_weight = sum(w * x for w, x in zip(w_values, x_values))
    total_price = sum(w * x * c for w, x, c in zip(w_values, x_values, c_values))
    return total_price, total_weight

def simulated_annealing(initial_temp, cooling_rate, iterations):
    current_x = [randint(0, 1) for _ in w_values]

    while sum(w * x for w, x in zip(w_values, current_x)) > MAX_WEIGHT:
        current_x[randint(0, len(current_x) - 1)] = 0

    current_price, current_weight = evaluate(current_x)
    best_x, best_price, best_weight = current_x[:], current_price, current_weight

    temp = initial_temp

    for _ in range(iterations):
        new_x = current_x[:]
        idx = randint(0, len(new_x) - 1)
        new_x[idx] = 1 - new_x[idx]

        new_price, new_weight = evaluate(new_x)

        if new_weight > MAX_WEIGHT:
            continue

        if new_price > current_price or random() < exp((new_price - current_price) / temp):
            current_x, current_price, current_weight = new_x, new_price, new_weight

            if new_price > best_price:
                best_x, best_price, best_weight = new_x[:], new_price, new_weight

        temp *= cooling_rate

    return best_x, best_price, best_weight

best_x_values, max_price, total_weight = simulated_annealing(initial_temp=100, cooling_rate=0.99, iterations=1000)

print(f"Максимальная ценность: {max_price:.2f}")
print(f"Вес набора: {total_weight}")
print(f"Оптимальный набор x: {best_x_values}")
