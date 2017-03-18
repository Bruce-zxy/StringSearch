#coding:utf-8

import os,sys
import re

s = os.sep

def walkFiles(root, string, count_num):
	for dirpath, dirname, filename in os.walk(root):
		for fn in filename:
			try:
				name = dirpath + s + fn
				# print "Searching file" + name
				flag = 0
				fp = open(name, 'r')
				count = 0
				for line in fp.readlines():
					count += 1
					if string in line:
						flag = 1
						print "Find string in file : %s in line %s, \nOriginal text is :%s" %(name,count,line)
					if flag == 0:
						pass
						# print "Nothing found"
				count_num += count
			except:
				print "File " + name + "can't be read"
	return count_num


def main(): 
	root = '/home'
	string = 'sublime_text'
	count_num = 0
	result = walkFiles(root, string, count_num)
	print "A total of %s rows in data searching" %result
	print 'Done'

if __name__ == '__main__':
	main()

