"""
找出10000以内的完美数
完美数：它所有的真因子（即除自身以外的因子）的和恰好等于它本身：
例如 6 = 1 + 2 + 3   28 = 1 + 2 + 4 + 7 + 14 就是完美数

Version: 1.0
Author: Tony
Date: 2021-01-15

"""

import math

for x in range(1, 10000):
    result = 0
    for y in range(1, int(x/2) + 1):
        if x%y == 0:
            result += y
    if result == x:
        print(x, end=', ')



