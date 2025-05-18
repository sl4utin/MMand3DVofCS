from math import *
from random import *


class Point:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point #{self.number} ({self.x}, {self.y})'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other) -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __hash__(self):
        return hash(f'{self.x}{self.y}')

    def calculate_range(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def calculate_sum_length(points: list[Point]):
    sum_range = 0
    for curr_index in range(len(points)):
        next_index = curr_index + 1
        if next_index >= len(points):
            next_index = 0

        sum_range += points[curr_index].calculate_range(points[next_index])
    return sum_range


def swap_random_points(points: list[Point]):
    first_index = randint(0, len(points) - 1)
    second_index = randint(0, len(points) - 2)

    if second_index >= first_index:
        second_index += 1
    if second_index >= len(points):
        second_index = 0

    tmp_point = points[first_index]
    points[first_index] = points[second_index]
    points[second_index] = tmp_point

    return points


def get_new_order(old_points: list[Point]):
    start_point = old_points[0]
    finish_point = old_points[-1]

    new_points = list()
    new_points.append(start_point)
    # [new_points.append(point) for point in swap_random_points(old_points[1:len(old_points)])]
    [new_points.append(point) for point in swap_random_points(old_points[1:len(old_points) - 1])]
    new_points.append(finish_point)

    return new_points


def get_new_tetta(start_omega, i):
    return start_omega * 0.1 / i


def get_swap_probability(diff, omega):
    return exp(- diff / omega)


def try_take_new_points(diff, omega):
    return random() < get_swap_probability(diff, omega)


def print_points(points: list[Point]):
    print(f'Сумма: {calculate_sum_length(points)}, точки: {points}')


POINTS = [
    Point(1, 1, 1),
    Point(2, 3, 7),
    Point(3, 5, 2),
    Point(4, 4, 5),
    Point(5, 3, 3),
    Point(6, 8, 4),
    Point(7, 9, 1),
    Point(8, 6, 8),
    Point(9, 6, 4),
    Point(10, 9, 7)
]


def main():
    global POINTS
    best_points = POINTS
    best_sum = calculate_sum_length(best_points)
    curr_points = POINTS

    print(f'Исходный маршрут:')
    print_points(curr_points)
    print()

    tettas = [50]
    for i in range(5):
        tettas.append(randint(1, 100))

    best_tetta = 0

    for tetta in tettas:
        curr_sum = calculate_sum_length(curr_points)
        for i in range(1, 5000):
            new_points = get_new_order(curr_points)
            new_sum = calculate_sum_length(new_points)

            if new_sum < best_sum:
                best_tetta = tetta
                best_points = new_points
                best_sum = new_sum

            if new_sum < curr_sum or try_take_new_points(new_sum - curr_sum, get_new_tetta(tetta, i)):
                curr_points = new_points
                curr_sum = new_sum

            print_points(curr_points)
    print()

    track = []
    for point in best_points:
        track.append(str(point.number))

    print(f'Лучший маршрут: {", ".join(track)}')
    print_points(curr_points)
    print(f'Лучшее значение тетта = {best_tetta} среди: {tettas}')


if __name__ == "__main__":
    main()
