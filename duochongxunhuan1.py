#coding:utf-8
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6

要求，只用while 和 print 语句
"""

#num = int(raw_input("please input num:"))
num = 7
i = 1
while i < num:
    i += 1
    j = 1
    while j < i:
        print j,
        j += 1
    print 