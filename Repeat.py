#! -*- coding:UTF-8 -*-
# Author="XB"

#Number not support

obuff = []
for ln in open('Input.txt'):
    if ln in obuff:
        continue
    obuff.append(ln)
with open('Output.txt', 'w') as handle:
    handle.writelines(obuff)

print "Remove Repeat Items Succeed."+"\n"
print "CopyRight@LogRead2017"
raw_input ("Press Enter To Exit. ")
