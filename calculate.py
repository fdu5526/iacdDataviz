#!/usr/bin/python

import os
import csv
import operator
from sets import Set


data = open('../../../../../tempData/10-million-combos.txt', 'r')
#data = open('blah.txt', 'r')
countDict = dict()
totalCountDict = dict()

for line in data:

	lineTokens = line.split('\t')

	# nonvalid input
	if(len(lineTokens) != 2):
		continue

	# password and username
	p = lineTokens[1]
	u = lineTokens[0]

	'''
	# first char
	uStart = u[0]
	
	# add password to count
	if p in countDict:
		if(uStart in countDict[p]):
			countDict[p][uStart] += 1
		else:
			countDict[p][uStart] = 1
	else:
		countDict[p] = { uStart : 1 }
	'''

	# add the password to totalCount
	if(p in totalCountDict):
		totalCountDict[p] += 1
	else:
		totalCountDict[p] = 1


# find the N most popular
sortedTotalCountDict = sorted(totalCountDict.items(), key=operator.itemgetter(1), reverse=True)
cherryPickedCountDict = dict()
i = 0
for key, val in sortedTotalCountDict:
	if(i == 10):
		break

	print(key)
	print(val)
	#cherryPickedCountDict[key] = countDict[key]
	i += 1

'''
# write values
w = csv.writer(open("output.csv", "w"))
for key, val in cherryPickedCountDict.items():
    w.writerow([key, val])
'''