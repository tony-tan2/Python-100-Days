"""
输出乘法口诀（九九表）

Version: 1.0
Author: Tony
Date: 2021-01-15
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%dx%d=%d' %(i, j, i*j), end='\t')
    print()