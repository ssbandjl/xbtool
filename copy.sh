#!/system/bin/sh

while true
do
#       busybox tar xvf a.tgz -C /dataflash
        busybox cp -a /mnt/sdcard/test/ /dataflash/
        sleep 1
done