#!/usr/bin/python
#coding=utf-8
'''
暂停1s输出
'''

import time
import sys


def printStar(n):
	for i in range(n):
		print " * ",
		sys.stdout.flush()
		time.sleep(1)

if __name__ == '__main__':
	printStar(10)
