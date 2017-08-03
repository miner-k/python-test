#!/usr/bin/python
#coding=utf-8

import math

def isSquNum(n):
	num = math.sqrt(n)
	return num.is_integer()

for i in range(10000):
	sum1 = i + 100
	sum2 = sum1 + 168
	if (isSquNum(sum1) and isSquNum(sum2)):
		print "this num is :%d" %i
