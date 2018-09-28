#!/bin/sh

set -e	#开启执行跟踪

if [ $# != 3 ]
then
   echo "Usage:$0 img.bin vdrup.bin timestamp."
else
   echo -e $3 > $2
   md5sum -b $1 >> $2
   cat $1 >> $2
fi
