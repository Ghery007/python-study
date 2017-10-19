# -*- coding:utf-8 -*-

def splitArray(array,start,end):
	if start < end:
		middle = int((end + start) / 2)
		splitArray(array,start,middle)
		splitArray(array,middle + 1,end)
		mergeArray(array,start,middle,end)
		
		
def mergeArray(array,start,middle,end):
	list = []
	fl = start
	sl = middle + 1
	while fl <= middle and sl <= end:
		if int(array[fl]) < int(array[sl]):
			list.append(array[fl]) 
			fl = fl + 1
		else:
			list.append(array[sl])
			sl = sl + 1
	
	while fl <= middle:
		list.append(array[fl]) 
		fl = fl + 1
			
	while sl <= end:
		list.append(array[sl])
		sl = sl + 1
		
	for temp in list:
		array[start] = temp
		start += 1
		
if __name__ == '__main__':
	list = [7,1,3,2,5,8,9,11,111,23,44,12,3,4,12,18,55,67,234567,345,678,98,88,90,88]
	splitArray(list,0,len(list) - 1)
	print(list)