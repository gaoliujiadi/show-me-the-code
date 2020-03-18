#writeXls.py
import xlwt
import os
path = "students.xls"
book = xlwt.Workbook(encoding="utf-8",style_compression=0)#初始化
sheet = book.add_sheet('students',cell_overwrite_ok=True)
with open('students.txt','r',encoding='utf-8') as f:
    lines = ''
    for line in f:
        lines = lines + line
    students = eval(lines)
for i in range(len(students.keys())):
    sheet.write(i,0,list(students.keys())[i])
    key = list(students.keys())[i]
    value = students[key]
    for j in range(len(value)):
        sheet.write(i,j + 1,value[j])
book.save('students.xls')
