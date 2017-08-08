#!/usr/bin/python
#coding=utf-8
'''
复制数组
'''

def cpList(l1):
	return l1[:]

if __name__ == '__main__':
	l1 = [1,2,3,45]
	l2 = cpList(l1)
	print l2
