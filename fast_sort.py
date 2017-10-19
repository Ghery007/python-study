#-*- coding:utf-8 -*-


def fastSort(array,start,end):
	if start < end:
		key = array[start]
		left_index = start
		right_index = end
		while(left_index < right_index):
			while right_index > left_index:
				if array[right_index] < key:
					array[left_index] = array[right_index]
					left_index += 1
					break
				right_index -= 1 
				
			while left_index < right_index:
				if array[left_index] > key:
					array[right_index] = array[left_index]
					right_index -= 1 
					break
				left_index += 1
					
		print(start,left_index,end)
		array[left_index] = key
		
		fastSort(array,start,left_index)
		fastSort(array,left_index + 1,end)
	


list = [7,1,3,2,5,8,9,11,111,23,44,12]
fastSort(list,0,len(list) - 1)
print(list)