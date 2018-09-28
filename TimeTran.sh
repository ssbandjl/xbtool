#! /bin/sh
# XB 2017/03

set -e

MergeRow(){
awk '{printf $0 ""} NR%5==0{print ""}' info.log>info_out.log	#NR表示已读的记录数，这里表示打印出5行后换行，即每5行合并为1行.
echo "MergeRow 5 To 1 Success."
}

TimestampTransform(){
while read myline
do
time=`echo $myline|awk -F '"' '{print$4}'`
Time=`date "+%Y-%m-%d %H:%M:%S" -d @$time`
echo $myline|sed "s/$time/$Time/g">>InfoOut.log		#将time替换成Time并追加文件中.
echo "Success `cat InfoOut.log|wc -l` Row."
done < info_out.log
}

MergeRow
TimestampTransform

