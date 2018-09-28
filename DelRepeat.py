#! -*- coding:UTF-8 -*-
# Author="XB"

obuff = []
for ln in open('Repeat.txt'):
    if ln in obuff:
        continue
    obuff.append(ln)
with open('RepeatOutput.txt', 'w') as handle:
    handle.writelines(obuff)

print "Remove Repeat Items Succeed."+"\n"
print "CopyRight@LogRead2017"
raw_input ("Press Enter To Exit. ")
