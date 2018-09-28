#!/bin/sh

. /lib/json/jshn.sh

Path="/extroot/extdata/test.log"
lon_base=119.370888
lat_base=32.420666

BDGPSTest(){
data=`ubus -S call gpsd gpsinfo`

json_set_namespace REQ
json_load "$data"
json_get_var lat lat
json_get_var latd latd
json_get_var lon lon
json_get_var lond lond
json_get_var speed speed
json_get_var time time
json_get_var elv elv
json_get_var count count
json_get_var visate visate
json_get_var status status


if [ "$status" = "A" ]
then
	echo $time
	
else
	distance=0
fi
}

main(){
while [ 1 ];
do
	BDGPSTest >> $Path                                                                                                                       
	#BDGPSTest                                                                                                                       
	sleep 1
done
}

main
