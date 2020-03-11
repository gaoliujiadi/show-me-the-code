#addActivationCodeToSQL.py

import random
import pymysql

SQL = pymysql.connect('localhost','root','meiyoumima1_1','pyExerDB')#连接数据库
cursor = SQL.cursor()#建立游标对象

#激活码
ls_o = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','$','%','&','?',]
ls = ls_o
lsAC = []
for i in range(10):
    random.shuffle(ls)
    ls_1 = ls[:10]
    AC = ''.join(ls_1)
    lsAC.append(AC)
strAC = ','.join(lsAC)

#数据库

cursor.execute("DROP TABLE IF EXISTS activationCodeDB;")

#创建表格
fuSQL = """CREATE TABLE activationCodeDB(
    ID int not null,
    ACode CHAR(10) not null
    );"""
cursor.execute(fuSQL)
#插入语句
fuSQL_EXC = 'INSERT INTO activationCodeDB (ID,ACode)\n'
for i in range(len(lsAC)):
    fuSQL_EXC_1 = fuSQL_EXC + 'VALUES (' + str(i + 1) + ',' + '\'' + lsAC[i] + '\'' + ');'
    print(fuSQL_EXC_1)
    cursor.execute(fuSQL_EXC_1)
    SQL.commit()

print('done')
SQL.close()
