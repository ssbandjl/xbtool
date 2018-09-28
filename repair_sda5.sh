#!/bin/sh

WEBROOT="/extroot/extdata/webroot"

TINY_URL="http://download.iovyw.com/airmedia-tiny-20170111.tar.xz"
TINY_TMP="$WEBROOT/airmedia-tiny-20170111.tar.xz"
STAMP="/tmp/.ssd_repair.lock"

do_exit(){
        echo "$1"
        rm -f $STAMP
        exit 0
}

########## check the sda5 is destroy or not ############
check_sda5_is_damage() {
        [ -e $STAMP ] && {
                echo "Previous check running"
                exit 0
        }
        touch $STAMP
        mount | grep sda5 2>/dev/null 1>&2 && do_exit "Disk check pass!"
        pidof btrfsck 2>/dev/null 1>&2 && do_exit "Disk is checking"
        [ -e /dev/sda5 ] || do_exit "sda5 not exists!"
        mount -t btrfs /dev/sda5 /mnt 2>/dev/null 1>&2 && {
                umount /mnt
                do_exit "sda5 remount success!"
        }
}

########## repair /dev/sda5 ###########################
format_mount_sda5() {
        mkfs.btrfs -f /dev/sda5
        ssdmanagle detach
        sleep 1
        ssdmanagle attach
mount | grep sda5 2>/dev/null 1>&2 || do_exit "mkbtrfs fail"    
}                                                                       
                                                                        
download_tiny_websit() {                                                
        local ret=""                                                    
                                                                        
        mkdir -p $WEBROOT                                               
                                                                        
        for i in 1 2 3                                                  
        do                                                              
                wget -c -q $TINY_URL -O $TINY_TMP 2>/dev/null 1>&2      
                ret="$?"                                                         
                [ "$ret" == "0" ] && break                              
        done                                                            
                                                                                 
        [ "$ret" != "0" ] &&  do_exit "download tiny websit from:$TINY_URL error"
}                                                                                
                                                                                 
apply_tiny_websit() {                                                            
        xzcat $TINY_TMP | tar -x -C $WEBROOT                                     
        [ "$?" != 0 ] && {                                                       
                rm $TINY_TMP -f                                                  
                do_exit "xz $TINY_TMP error"                                     
        }                                                                        
        touch $WEBROOT/.tiny_fix                                                 
        /etc/init.d/nginx restart                                                
        do_exit "upgrade tiny ok"                                                
}                                                                                
                                                                                 
main() {                                                                         
#       format_mount_sda5                                                        
        download_tiny_websit                                                     
        apply_tiny_websit                 }                                                                                
                                                                                 
#check_sda5_is_damage                                                            
echo "begin repair sda5"                                                         
main &    