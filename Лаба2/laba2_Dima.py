import random
import math
from collections import OrderedDict
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def calculate_func(points):
    total_distance = 0.0
    points_list = list(points.values())

    # Calculate distance between consecutive points
    for i in range(len(points_list) - 1):
        total_distance += points_list[i].distance(points_list[i + 1])

    # Add distance back to the starting point
    total_distance += points_list[-1].distance(points_list[0])

    return total_distance


def change_points(points):
    points_dict = points.copy()
    keys = list(points_dict.keys())

    # Select two random indices to swap (excluding first point if needed)
    idx1, idx2 = random.sample(range(1, len(keys) - 1), 2)

    # Swap the keys
    keys[idx1], keys[idx2] = keys[idx2], keys[idx1]

    # Create new ordered dictionary with swapped keys
    new_points = OrderedDict()
    for key in keys:
        new_points[key] = points_dict[key]

    return new_points


def algorithm(points, teta0):
    min_distance = float('inf')
    best_path = None
    current_points = points.copy()

    for _ in range(10):
        for i in range(1, 500000):
            f1 = calculate_func(current_points)
            new_points = change_points(current_points)
            f2 = calculate_func(new_points)

            if f1 > f2:
                current_points = new_points
            else:
                teta = teta0 / i
                p = math.exp(-(f2 - f1) / teta)
                if random.random() < p:
                    current_points = new_points

        current_distance = calculate_func(current_points)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = current_points.copy()

    print(f"Minimum distance: {min_distance}")
    print(f"Best path order: {list(best_path.keys())}")


def main():
    points = OrderedDict({
        1: Point(1, 1),
        2: Point(3, 7),
        3: Point(5, 2),
        4: Point(4, 5),
        5: Point(3, 3),
        6: Point(8, 4),
        7: Point(9, 1),
        8: Point(6, 8),
        9: Point(6, 4),
        10: Point(9, 7)
    })

    algorithm(points, 50)


if __name__ == "__main__":
    main()