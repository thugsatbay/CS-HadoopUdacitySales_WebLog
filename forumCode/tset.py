#!/usr/bin/python

import csv
import sys

file=open("../forumData/forum_node.tsv","rb")
reader=csv.reader(file,delimiter="\t")
for line in reader:
	print line
	break

