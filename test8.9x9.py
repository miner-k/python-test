#!/usr/bin/python
#coding=utf-8
'''
打印 9*9 乘法表
'''

def mult_table(n):
	for i in range(1,n+1):
		for j in range(1,i+1):
			if i == j:
				print "%d x %d = %-2d " %(i,j,i*j)
			else:
				print "%d x %d = %-2d " %(i,j,i*j),

if __name__ == '__main__':
	mult_table(9)
