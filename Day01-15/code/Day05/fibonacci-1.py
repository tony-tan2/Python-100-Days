"""
斐波那契数列，前两个数都是1，从第三个数起每个数都是前面两个数的和

Version: 1.0
Author: Tony
Date: 2020-01-15
"""

a = 0
b = 1
for i in range(0, 20):
    a, b = b, a + b
    print(a, end= ', ')

