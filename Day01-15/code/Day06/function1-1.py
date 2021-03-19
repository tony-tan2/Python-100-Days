"""
函数的定义和使用 - 计算组合数C(7,3)

Version: 0.1
Author: Tony
Date: 2021-03-13
"""

m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num

fn = 1
for num in range(1, n + 1):
    fn *= num

fm_n = 1
for num in range(1, m - n + 1):
    fm_n *= num

print(fm // fn // fm_n)



