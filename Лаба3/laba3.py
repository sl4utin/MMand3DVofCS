from math import *
from random import *

w_values = [4,   6,   2,   8,   9,   1,   3,   5,   4,   3  ]
c_values = [5.0, 4.5, 6.0, 4.0, 3.5, 7.0, 4.0, 3.0, 6.5, 5.5]


max_value = 0
MAX_WEIGHT = 32
max_x_values = []

for i in range(1000):
    x_values = [(randint(0, 1)) for x in range(len(w_values))]

    total_weight = sum(w * x for w, x in zip(w_values, x_values))
    if total_weight <= MAX_WEIGHT:
        total_price = sum(w * x * c for w, x, c in zip(w_values, x_values, c_values))

