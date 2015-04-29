#coding:utf-8
"""
递推法:递推法实际上是一种递推关系。在不少计数问题中，要很快求出结果是比较困难的，有时可先从简单情况入手，
然后从某一种特殊情况逐渐推出与以后比较复杂情况之间的关系，找出规律逐步解决问题，这样的方法叫递推方法。

就是为了得到问题的解，把它推倒比原问题简单的问题求解，可分为顺推法和倒推法。

1 顺推法，就是先找到递推关系式，然后从初始条件出发，一步步地按递推关系式递推，直至求出最终结果。
2 倒推法，就是在不知道初始条件的情况下，经某种递推关系而获知问题的解，再倒过来，推知它的初始条件。

递推法 求阶乘
1！ + 2！ + 3！ + 4！ + 5！ + 6！ + ...... + n! 
"""

total = 0
t = 1
n = int(raw_input("Please input n:\n"))

for i in xrange(1, n+1):
    t = t * i
    total += t

print "total=%d" % total
