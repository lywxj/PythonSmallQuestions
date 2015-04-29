#coding:utf-8
"""
guess number
"""

import random
import string

thenum = random.randint(0,100)
print thenum

while True:
    guess = raw_input("please input guess:\n")
    print type(thenum)
    print type(guess)
    if guess.isdigit():
        if int(guess) == thenum:
            print '恭喜答对了!'
            break
        elif int(guess) < thenum:
            print '输入的数字太小！'
        else:
            print '输入的数字太大！'
    else:
        print "你输入的是字符串，请输入数字！"
    