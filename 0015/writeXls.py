#writeXls.py
import xlwt
path = 'city.xls'
book = xlwt.Workbook(encoding="utf-8",style_compression=0)
sheet = book.add_sheet('city',cell_overwrite_ok=True)
with open('city.txt','r',encoding='utf-8') as f:
    lines = ''
    for line in f:
        lines = lines + line
    city = eval(lines)
for i in range(len(city.keys())):
    sheet.write(i,0,list(city.keys())[i])
    key = list(city.keys())[i]
    value = city[key]
    sheet.write(i,1,value)
book.save(path)