##writeXls.py
import xlwt
path = 'numbers.xls'
book = xlwt.Workbook(encoding="utf-8",style_compression=0)
sheet = book.add_sheet('city',cell_overwrite_ok=True)
with open('numbers.txt','r',encoding='utf-8') as f:
    lines = ''
    for line in f:
        lines = lines + line
    numbers = eval(lines)
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        sheet.write(i,j,numbers[i][j])
book.save(path)