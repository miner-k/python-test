#!/usr/bin/python
#coding=utf-8

import time
import calendar

year = input("Plz input the number of year:")
month = input("Plz input the number of month:")
day = input("Plz input the number of day:")


def getDays():
	
	star = calendar.timegm((year,1,1,0,0,0))
	end = calendar.timegm((year,month,day,0,0,0))
	return (end - star)/3600/24 + 1

print getDays()

