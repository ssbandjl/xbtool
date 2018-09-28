#!/usr/bin/env python
#XB 17/9

import sys,getopt

list1=[]
list2=[]


def getinput(a,b):
        with open(a,'r') as f:
        #with open('sysupgrade_done_sn.txt','r') as f:
                for line in f:
                        sn=line.strip()
                        list1.append(sn)
        
	with open(b,'r') as f:
        #with open('add_sysupgrade_sn.txt','r') as f:
                for line in f:
                        sn=line.strip()
                        list2.append(sn)

def intersection_set():
	result_list=list(set(list1).intersection(set(list2)))
	for result in result_list:
		print (result)

def difference_set():
	result_list=list(set(list1).difference(set(list2))) #list1 - list2
	for result in result_list:
		print (result)


if __name__ == '__main__':
	getinput(sys.argv[1],sys.argv[2])
	#intersection_set()
	difference_set()

