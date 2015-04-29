#coding:utf-8
"""
author:etoo
date:20130912
百钱买百鸡，公鸡一，值5钱；母鸡一，值3钱；小鸡三，值1钱，百钱买百鸡，问，公鸡，母鸡，小鸡 各几只？？？
x is 公鸡
y is 母鸡
z is 小鸡
0 =< x <= 20 公鸡最多20支
0 =< y <= 33 母鸡最多33支
x + y + z = 100
5x + 3y + z/3 = 100
"""
if __name__ == '__main__':
    for x in xrange(21):
        for y in xrange(34):
            z = 100 - x - y
            if z%3 ==0 and x+y+z ==100 and 5*x + 3*y + z/3 == 100:
                print '公鸡 %d 只， 母鸡 %d 只， 小鸡 %d 只' % (x,y,z) 
