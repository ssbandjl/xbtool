##!/usr/bin/env python
# _*_ coding: utf-8 _*_
#XB 17/10

def dectohex(input):
	input=int(input)
	my_hex=hex(input)
	my_return=my_hex.replace('0x','')
	return my_return


def utf8_gb2312_hex(input):
	#my_utf8=input.decode('utf8')
	my_gb2312=input.encode('gb2312')
	my_hex=my_gb2312.encode('hex')
	return my_hex




