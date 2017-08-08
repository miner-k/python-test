#!/usr/bin/python
#coding=utf-8

def fib(n):
	if n == 2:
		return 1
	if n == 1:
		return 0
	if n > 2:
		return fib(n-2) + fib(n-1)

print fib(10)
