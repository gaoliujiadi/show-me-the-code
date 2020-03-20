#xlsToXml.py
import xlrd
import xml.dom.minidom as md
workbook = xlrd.open_workbook('students.xls')
sheet = workbook.sheet_by_index(0)
keys = sheet.col_values(0)
dic = {}

for i in range(sheet.nrows):
    values = sheet.row_values(i)[1:]
    dic[keys[i]] = values

dicStr = str(dic)

xmlFile = md.Document()#创建
root = xmlFile.createElement('root')#创建节点
students = xmlFile.createElement('students')#创建节点

xmlFile.appendChild(root)#在文件中添加root节点
root.appendChild(students)#在root下添加students节点
students.appendChild(xmlFile.createComment('学生信息表 "id" : [名字, 数学, 语文, 英文]'))#在students标签下添加comment

students.appendChild(xmlFile.createTextNode(dicStr))#文本节点

with open('students.xml', 'wb') as f:
    f.write(xmlFile.toprettyxml(encoding='utf-8'))