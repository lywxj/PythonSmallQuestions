#coding:utf-8
"""
完全数：是一个整数，其因数的和（不包含本身的因素）就是本身。
下面是 4 个 完全数示例。
6 = 1 + 2 + 3
28 = 1 + 2 + 4 + 7 + 14
496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 
8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 +508 + 1-16 +2032 +4064
用程序判断一个数是不是完全数。 
1 获取数字
thenum = raw_input("请输入一个整数待检查是不是完全数") thenum = int(thenum)
2 查找因子
因数是能整除数thenum的数 thenum%d==0那么d是thenum的因子
用一个while 循环 d 从 1 到 thenum, 输出 thenum %d == 0 的d
3 将所有 d 加和 和 thenum 比较，如果相等则为 完全数。
"""

thenum = int(raw_input('请输入一个数:\n'))

sum = 0
jishu = 1
while jishu < thenum:
    if thenum % jishu == 0:
        sum += jishu
    jishu += 1
if sum == thenum:
    print str(thenum) + "是完全数"
else:
    print str(thenum) + "不是完全数"


