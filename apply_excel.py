'''
作者： 张启卫
时间： 2018年12月5号
功能：Python 处理Excel 文件
参考文档： http://www.python-excel.org/

xlrd
	pip install xlrd
wlwt
	pip install xlwt

'''

import xlrd
import xlwt

filename1 = '26120181204215349258-1.xls'
filename2 = '26120181204215349258-2.xls'
filename3 = '26120181204215349258-3.xls'
filename4 = '26120181204215349258-4.xls'
ret_file = 'suning-product.xls'

workbook1 = xlrd.open_workbook(filename1)
workbook2 = xlrd.open_workbook(filename2)
workbook3 = xlrd.open_workbook(filename3)
workbook4 = xlrd.open_workbook(filename4)

sheet_names1 = workbook1.sheet_names()
sheet_names2 = workbook2.sheet_names()
sheet_names3 = workbook3.sheet_names()
sheet_names4 = workbook4.sheet_names()


worksheet1 = workbook1.sheet_by_name(sheet_names1[0])
worksheet2 = workbook2.sheet_by_name(sheet_names2[0])
worksheet3 = workbook3.sheet_by_name(sheet_names3[0])
worksheet4 = workbook4.sheet_by_name(sheet_names4[0])

#苏宁商品编码
suningID_list1 = worksheet1.col_values(2)
suningID_list2 = worksheet2.col_values(2)
suningID_list3 = worksheet3.col_values(2)
suningID_list4 = worksheet4.col_values(2)
#淘宝商品编码
taobaoID_list1 = worksheet1.col_values(7)
taobaoID_list2 = worksheet2.col_values(7)
taobaoID_list3 = worksheet3.col_values(7)
taobaoID_list4 = worksheet4.col_values(7)


workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('product')

# 表示行数
i = 0 
# 表示写入行数
j = 0

for suningID in suningID_list1:
	taobaoID = worksheet1.cell(i, 7).value
	status = worksheet1.cell(i, 11).value
	time = worksheet1.cell(i, 12).value
	if taobaoID != '' and status == '在售':
		worksheet.write(j,0,suningID)
		worksheet.write(j,1,taobaoID)
		worksheet.write(j,2,time)
		j += 1
	i += 1

i = 0
for suningID in suningID_list2:
	taobaoID = worksheet2.cell(i, 7).value
	status = worksheet2.cell(i, 11).value
	time = worksheet2.cell(i, 12).value
	if taobaoID != '' and status == '在售':
		worksheet.write(j,0,suningID)
		worksheet.write(j,1,taobaoID)
		worksheet.write(j,2,time)
		j += 1
	i += 1

i = 0
for suningID in suningID_list3:
	taobaoID = worksheet3.cell(i, 7).value
	status = worksheet3.cell(i, 11).value
	time = worksheet3.cell(i, 12).value
	if taobaoID != '' and status == '在售':
		worksheet.write(j,0,suningID)
		worksheet.write(j,1,taobaoID)
		worksheet.write(j,2,time)
		j += 1
	i += 1

i = 0
for suningID in suningID_list4:
	taobaoID = worksheet4.cell(i, 7).value
	status = worksheet4.cell(i, 11).value
	time = worksheet4.cell(i, 12).value
	if taobaoID != '' and status == '在售':
		worksheet.write(j,0,suningID)
		worksheet.write(j,1,taobaoID)
		worksheet.write(j,2,time)
		j += 1
	i += 1

workbook.save(ret_file)

