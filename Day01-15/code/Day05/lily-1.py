
"""
找出100 ~ 999之间的所有水仙花数，该数字每个位上数字的立方之和正好等于它本身
例如 1**3 + 5**3 + 3**3 = 153

Version: 0.1
Author:  Tony
Date:    2021-01-08
"""

for num in range(100, 999):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print (num)
    else:
        continue


