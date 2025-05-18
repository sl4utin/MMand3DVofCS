import math
import random
from random import randint


class Point:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def __repr__(self):
        return f'Point({self.x1}, {self.x2}, {self.x3})'

    def __str__(self):
        return self.__repr__()

    def get_func_value(self):
        return func(self.x1, self.x2, self.x3)

    def check_conditions(self, x_min, x_max) -> bool:
        if self.x1 < x_min or self.x1 > x_max:
            return False
        if self.x2 < x_min or self.x2 > x_max:
            return False
        if self.x3 < x_min or self.x3 > x_max:
            return False

        return True

    def clip(self, x_min, x_max):
        if self.x1 < x_min:
            self.x1 = x_min
        if self.x1 > x_max:
            self.x1 = x_max

        if self.x2 < x_min:
            self.x2 = x_min
        if self.x2 > x_max:
            self.x2 = x_max

        if self.x3 < x_min:
            self.x3 = x_min
        if self.x3 > x_max:
            self.x3 = x_max

    def __eq__(self, other) -> bool:
        if self.x1 == other.x1 and self.x2 == other.x2 and self.x3 == other.x3:
            return True
        return False

    def __hash__(self):
        return hash(f'{self.x1}{self.x2}{self.x3}')


def point_by_angle_and_length(point: Point, ang_xy, ang_z, length):
    # return Point(point.x1, point.x2, point.x3 - STEP)
    hyp = length
    x1 = math.cos(ang_xy) * hyp
    x2 = math.sin(ang_xy) * hyp
    x3 = math.sin(ang_z) * hyp
    return Point(point.x1 + x1, point.x2 + x2, point.x3 + x3)


def get_new_point(point, step, prev_func_value):
    global N, x_min, x_max

    for i in range(N):
        rand_angle_xy = random.uniform(0, 1) * 2 * math.pi
        rand_angle_z = random.uniform(0, 1) * 2 * math.pi
        new_point = point_by_angle_and_length(point, rand_angle_xy, rand_angle_z, step)
        new_point.clip(x_min, x_max)
        if new_point.get_func_value() > prev_func_value and new_point.check_conditions(x_min, x_max):
            return new_point
        if random.random() < 1:#0.1:
            return point

    return point


def func(x1, x2, x3):
    return (x1 - 15) ** 2 + (x2 - 3) ** 2 + x3
    # return 2 * x1 ** 2 + 2 * x1 + 4 * x2 - 3 * x3


x_min = 0
x_max = 10
STEP = 0.001
N = 100
M = 60000

def main():
    global M, STEP

    result_points = []
    points_count = 1
    start_point = Point(randint(x_min, x_max), randint(x_min, x_max), randint(x_min, x_max))
    # start_point = Point(10, 10, 10)
    for try_number in range(1, points_count + 1):
        point = start_point
        print(f'Стартовая точка №{try_number}: {point}, её значение: {point.get_func_value()}')

        for i in range(M):
            point = get_new_point(point, STEP, point.get_func_value())
            print(f'Промежуточная точка №{try_number}, {i}: {point}, её значение: {point.get_func_value()}')

        result_points.append(point)
        print(f'Конечная точка №{try_number}: {point}, её значение: {point.get_func_value()}')
        print()

    print(f"{result_points}")
    print()


if __name__ == "__main__":
    main()
