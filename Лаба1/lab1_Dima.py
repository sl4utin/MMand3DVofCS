import random
import math

random.seed()


class Vector:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def getX1(self):
        return self.x1

    def getX2(self):
        return self.x2

    def getX3(self):
        return self.x3


def generate_vector():
    x1 = random.uniform(0, 10)
    x2 = random.uniform(0, 10)
    x3 = random.uniform(0, 10)
    return Vector(x1, x2, x3)


def func(vector):
    return 2 * math.pow(vector.getX1(), 2) + 2 * vector.getX1() + 4 * vector.getX2() - 3 * vector.getX3()


def vector_len(vector):
    return abs(math.pow(vector.getX1(), 2) + math.pow(vector.getX2(), 2) + math.pow(vector.getX3(), 2))


def generate_new_x(x0, a):
    x = generate_vector()
    vector_len_val = vector_len(x)

    phi = random.randint(0, 360)
    s = random.randint(0, 360)

    n1 = math.cos(math.radians(phi))
    n2 = math.sin(math.radians(phi))
    n3 = math.cos(math.radians(s))

    x1 = x0.getX1() + a * n1
    x2 = x0.getX2() + a * n2
    x3 = x0.getX3() + a * n3

    if x1 > 10 or x1 < 0 or x2 > 10 or x2 < 0 or x3 > 10 or x3 < 0:
        return generate_new_x(x0, a / 2)

    return Vector(x1, x2, x3)


def alg(a, N, M):
    x0 = Vector(5.2, 9.4, 3.4)
    f0 = func(x0)

    for i in range(M + 1):
        errors = 0
        while errors <= N:
            x1 = generate_new_x(x0, a)
            f1 = func(x1)

            if f1 <= f0:
                errors += 1
            else:
                x0 = x1
                f0 = f1
                print(f"{x1.getX1()} {x1.getX2()} {x1.getX3()}")
                print(f1)
                break

        if errors > N:
            break

    return f0


def main():
    N = 1000
    a = 1
    M = 100000
    max_val = alg(a, N, M)
    print(max_val)


if __name__ == "__main__":
    main()