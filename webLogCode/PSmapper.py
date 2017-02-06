#!/usr/bin/python
import sys

def itemMapper():
	for eachLine in sys.stdin:
		data = eachLine.strip().split("\t")
		if len(data)==6:
			date,time,store,item,cost,payment=data
			print "{0}\t{1}".format(item,cost)
	

def storeMapper():
	for eachLine in sys.stdin:
		data = eachLine.strip().split("\t")
		if len(data)==6:
			date,time,store,item,cost,payment=data
			print "{0}\t{1}".format(store,cost)


storeMapper()
