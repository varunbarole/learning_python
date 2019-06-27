import os
import re

vlst1 = os.listdir(path="/home")
vlst2 = os.listdir(path="/video")

#print(vlst1)

#for lst1 in vlst1:
#    lst1
#    #print(lst1)
#
#for lst2 in vlst2:
#    lst2
#    #print(lst2)

for lst1,lst2 in zip(vlst1,vlst2):
    #print("%s,%s"%(lst1,lst2))
    lst11 = lst1.strip()
    lst22 = lst2.strip()
    #print (re.sub(' +',' ',lst11 + lst22))
    pvalf = print(lst1,',',lst2,sep="")