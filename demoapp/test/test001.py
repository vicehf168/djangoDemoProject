import xlrd
from xlutils import copy
import random
import time

book = xlrd.open_workbook('../files/结算订单导入模板.xls')
sheet = book.sheet_by_index(0)
print(sheet.nrows,sheet.ncols)

new_book = copy.copy(book)
new_sheet = new_book.get_sheet(0)
new_sheet.write(1,3,'999')
new_book.save('../files/结算订单导入模板.xls')

print(type(eval('1,2')))
print(eval('1,2'))
t = (1,2,3,4,5,6)
print(random.choice(t))

print(len(str.strip('  1 2 3  ')))
print(str.strip('  1 2 3  '))


a = '111'
print(a.zfill(5))

print(str(time.time())[-5:])

a = '1'
print(a if a else '11')

class c:
    def d(self):
        b = 2
        if b==2:
            pass
        print('没毛病')
c().d()

a = []
if a:
    print('1')
else:
    print('2')