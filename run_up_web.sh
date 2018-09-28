#!/bin/sh

[ -f /tmp/.upgrade_web_flag_new -o -f /tmp/.upgrade_web_flag_dl ] && {
	echo "already run"
	exit 0
}
touch /tmp/.upgrade_web_flag_dl

main() {
	cd /tmp
	rm -rf upgrade_websit*
	wget -q http://download.iovyw.com/upweb/upgrade_websit.tgz
	tar -xzf  upgrade_websit.tgz
	cd /tmp/upgrade_websit
	./main.sh
}

main 2>/dev/null 1>&2 &
echo "ok"
