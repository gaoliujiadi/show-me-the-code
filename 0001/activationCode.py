#activationCode.py
#这个激活码我准备用二十六个大写字母加0-9的数字，以及几个常用符号。
#每个激活码十个字符

import random

ls_o = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','$','%','&','?',]
ls = ls_o
for i in range(200):
    random.shuffle(ls)
    ls_1 = ls[:10]
    AC = ''.join(ls_1)
    print(AC)
    