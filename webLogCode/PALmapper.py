#!/usr/bin/python
import sys

def requestAL():
	for eachLine in sys.stdin:
		data=eachLine.strip().split(" ")
		if len(data)==10:
			ip,identity,username,time,zone,method,request,protocol,status,size=data
			if len(request.split("/")[-1])!=0:
				print request.split("/")[-1],request.replace("http://www.the-associates.co.uk","")

requestAL()
				
