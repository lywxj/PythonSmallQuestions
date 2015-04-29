#coding:utf-8
"""
求圆周率pi的问题
pi = 4/1 -4/3 + 4/5 -4/7 + ...
直到最后一项的绝对值小于10的-6次方为止。
"""
import math
flag = 4.0
sumpi = 0
n = 1
while math.fabs(flag/(n+n-1)) >= 1e-6:
    sumpi += flag/(n+n-1)
    n += 1
    flag = -flag
    
print sumpi
