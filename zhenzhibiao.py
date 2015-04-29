#coding:utf-8
"""
真值表
"""

print "p           q      p and q      p or q"

length = len("p           q      p and q      p or q")
print '-' * length

for p in [True, False]:
    for q in [True, False]:
        print '%-9s %-9s %-9s %-9s' % (p,q,(p and q), (p or q))

#learning python 操作符。140页

