from math import *
from random import *


class Item:
    def __init__(self, number, w, c):
        self.number = number
        self.w = w
        self.c = c

    def __repr__(self):
        return f'Item #{self.number} (w = {self.w}, c = {self.c})'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other) -> bool:
        if self.w == other.w and self.c == other.c:
            return True
        return False

    def __hash__(self):
        return hash(f'{self.w}{self.c}')

    def calculate_price(self):
        return self.w * self.c


def aim_func(order: list[int]):
    global ITEMS
    aim_func_sum = 0
    for i in range(len(order)):
        aim_func_sum += ITEMS[i].calculate_price() * order[i]
    return aim_func_sum


def swap_random_items(items: list[Item]):
    first_index = randint(0, len(items) - 1)
    second_index = randint(0, len(items) - 2)

    if second_index >= first_index:
        second_index += 1
    if second_index >= len(items):
        second_index = 0

    tmp_item = items[first_index]
    items[first_index] = items[second_index]
    items[second_index] = tmp_item

    return items


def get_new_order(n: int):
    return [randint(0, 1) for _ in range(n)]


def get_new_tetta(start_omega, i):
    return start_omega * 0.1 / i


def get_swap_probability(diff, omega):
    return exp(- diff / omega)


def try_take_new_order(diff, omega):
    return random() < get_swap_probability(diff, omega)


def is_order_compatible(order: list[int]):
    global ITEMS, MAX_WEIGHT
    items = ITEMS
    weight_sum = 0
    for i in range(len(order)):
        weight_sum += items[i].w * order[i]
    return weight_sum <= MAX_WEIGHT


def print_order(order: list[int]):
    print(f'Сумма: {aim_func(order)}, порядок: {order}')


ITEMS = [
    Item(1, 4, 5),
    Item(2, 6, 4.5),
    Item(3, 2, 6),
    Item(4, 8, 4),
    Item(5, 9, 3.5),
    Item(6, 1, 7),
    Item(7, 3, 4),
    Item(8, 5, 3),
    Item(9, 4, 6.5),
    Item(10, 3, 5.5)
]
TETTA = 2
MAX_WEIGHT = 32


def main():
    global TETTA
    curr_order = get_new_order(len(ITEMS))

    print(curr_order)
    print(aim_func(curr_order))

    for i in range(1, 5000):
        new_order = get_new_order(len(ITEMS))
        new_aim_func_value = aim_func(new_order)

        if not is_order_compatible(new_order):
            continue

        if new_aim_func_value > aim_func(curr_order) or try_take_new_order(aim_func(curr_order) - new_aim_func_value, get_new_tetta(TETTA, i)):
            curr_order = new_order

        print(f'Итерация №{i}:')
        print_order(curr_order)


if __name__ == "__main__":
    main()
