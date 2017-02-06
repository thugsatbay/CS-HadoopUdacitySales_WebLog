#!/usr/bin/python

import sys

def maxHours(dict):
	listElements = []
	maxPosts = 0
	for x in dict.keys():
		if maxPosts < dict[x]:
			maxPosts = dict[x]
	for x in dict.keys():
		if maxPosts == dict[x]:
			listElements.append(x)
	return listElements


def reducerForum():
	currentKey,dic=None,{} 
	for eachLine in sys.stdin:
		dataMapped = eachLine.strip().split(" ")
		if len(dataMapped)!=2:
			continue
		thisKey,thisValue=dataMapped
		if currentKey==None or currentKey!=thisKey:
			if currentKey != None:
				print currentKey,", ".join(map(str,maxHours(dic)))
			currentKey=str(thisKey)
			dic={}
		if thisValue in dic.keys():
			dic[thisValue]=dic[thisValue]+1
		else:
			dic[thisValue]=1
	if currentKey!=None:
 		print currentKey,", ".join(map(str,maxHours(dic)))



reducerForum()
