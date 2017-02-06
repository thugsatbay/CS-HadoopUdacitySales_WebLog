#!/usr/bin/python
import sys

	
def sumValuesPerKey():
	oldKey,TotalSales=None,0
	for eachLine in sys.stdin:
		dataMapped=eachLine.strip().split("\t")
		if len(dataMapped)!=2:
			continue
		thisKey,thisValue=dataMapped
		if oldKey and oldKey!=thisKey:
			print oldKey, "\t",TotalSales
			oldKey = thisKey
			TotalSales=0
		oldKey=thisKey
		TotalSales+=float(thisValue)
	
	if oldKey!=None:
		print oldKey,"\t",TotalSales


def highestValuePerKey():
	oldKey,HighestSale=None,0.0	
	for eachLine in sys.stdin:
		dataMapped=eachLine.strip().split("\t")
		if len(dataMapped)!=2:
			continue
		thisKey,thisValue=dataMapped
		if oldKey and oldKey!=thisKey:
			print oldKey, "\t",HighestSale
			oldKey = thisKey
			HighestSale=0.0
		oldKey=thisKey
		if float(thisValue) > HighestSale:
			HighestSale=float(thisValue)
	
	if oldKey!=None:
		print oldKey,"\t",HighestSale


def totalValue():
	TotalSale,TotalSaleValue=0,0.0	
	for eachLine in sys.stdin:
		dataMapped=eachLine.strip().split("\t")
		if len(dataMapped)!=2:
			continue
		thisKey,thisValue=dataMapped
		TotalSale+=1
		TotalSaleValue+=float(thisValue)
	
	if TotalSale!=0:
		print TotalSale,"\t",TotalSaleValue


totalValue()
