#!/bin/sh

tmp=0
t=0

cat /extroot/extdata/test.log | while read line
do 
	time=`echo $line | awk -F ' ' '{print $2}'`
	#echo $time
	
	va=`echo $time | awk -F ':' '{print $3}'`
	#echo $va
	
	#diff=$((va-tmp))
	diff=`expr $va - $tmp`
	#echo $diff
	
	tmp=$va
	if [ $diff -eq $t ] 
	then
		echo $line	
	fi
	#echo $tmp
done

