#!/usr/bin/python
import sys

def requestReducer(keyToBeFound):
	hits=0
	for eachLine in sys.stdin:
		dataMapped=eachLine.strip().split(" ")
		if len(dataMapped)!=2:
			continue
		thisKey,thisValue=dataMapped
		if str(keyToBeFound) in str(thisKey):
			hits+=1

	print hits


def mostPopular():
	pathMostPopular,currentKey,hits,maxHits=None,None,0,0
	for eachLine in sys.stdin:
		dataMapped=eachLine.strip().split(" ")
		if len(dataMapped)!=2:
			continue
		thisKey,thisValue=dataMapped
		if currentKey==None or currentKey!=thisKey:
			hits=0
			currentKey=str(thisKey)
		hits+=1
		if hits > maxHits:
			maxHits=hits
			pathMostPopular=str(thisValue)

	print pathMostPopular,maxHits



mostPopular()
'''
requestKey="10.99.99.186"
requestReducer(requestKey)
'''
