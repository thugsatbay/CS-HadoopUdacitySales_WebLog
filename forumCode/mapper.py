#!/usr/bin/python

import sys
import csv

def mapperForum():
	columnNames=['id', 'title', 'tagnames', 'author_id', 'body', 'node_type', 'parent_id', 'abs_parent_id', 'added_at', 'score', 'state_string', 'last_edited_id', 'last_activity_by_id', 'last_activity_at', 'active_revision_id', 'extra', 'extra_ref_id', 'extra_count', 'marked']
	reader=csv.reader(sys.stdin , delimiter="\t")
	for eachLine in reader:
		if str(eachLine[0]) == str(columnNames[0]):
			continue
		print eachLine[3],eachLine[8].split(" ")[1].split(":")[0]


mapperForum()
