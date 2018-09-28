#!/usr/bin/env python

import requests

def devStatus():
    url = "http://hm.iovyw.com/platform/res/rpc.do?method=list"
    r = requests.get(url).text
    print r
    allList = r.split("\n")
    allList = [dev.split(",") for dev in allList]
    devSN = onLine = offLine = noReg = disconnect = []
    noReg = [x[0] for x in allList if len(x) == 3 and x[1] == "0"]
    onLine = [x[0] for x in allList if len(x) == 3 and x[1] == "1"]
    disconnect = [x[0] for x in allList if len(x) == 3 and x[1] == "2"]
    offLine = [x[0] for x in allList if len(x) == 3 and x[1] == "3"]
    #return allList, devSN, noReg, onLine, disconnect, offLine  
    #for i in onLine:
    #   print i

def chkOnline(sn):
    url = "http://hm.iovyw.com/platform/res/rpc.do?method=list&param="
    r = requests.get(url + sn).text
    return r.split(",")[1]

if __name__== "__main__":
    devStatus()