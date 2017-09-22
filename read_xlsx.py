#-*- coding:utf-8 -*-

import xlrd

def read_xlsx(file_name):
	if file_name:
		wbook = xlrd.open_workbook(file_name)
		sheets_num = wbook.nsheets
		print("sheet number is ",sheets_num)
		sheet1 = wbook.sheet_by_name("SAMPLE")
		print('this have rows number is ',sheet1.nrows)
		print('this have cols number is ',sheet1.ncols)
		for row_index in range(1,sheet1.nrows):
			print(sheet1.cell_value(row_index,0))
			


if __name__=="__main__":
	print("*********start process***********")
	read_xlsx("d://a.xlsx")