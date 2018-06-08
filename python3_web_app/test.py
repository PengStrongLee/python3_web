# !/usr/bin/python3
# -*- coding: UTF-8 -*-

import collections
import time
import re

class UserInfo(object):
    'Class to restore UserInformation'
    def __init__ (self):
        self.attrilist=collections.OrderedDict()# ordered
        self.__attributes=[]
    def updateAttributes(self,attributes):
        self.__attributes=attributes
    def updatePairs(self,values):
        for i in range(len(values)):
            self.attrilist[self.__attributes[i]]=values[i]

def catchTime(item):
    # check if it's time
    matchObj=re.match(r'\d{4}-\d{2}-\d{2}',item, flags= 0)
    if matchObj!= None :
        item =time.strptime(item,'%Y-%m-%d')
        #print "returned time: %s " %item
        return item
    else:
        matchObj=re.match(r'\d{4}/\d{2}/\d{2}\s\d+:\d+:\d+',item,flags=0 )
        if matchObj!= None :
            item =time.strptime(item,'%Y/%m/%d %H:%M:%S')
            #print "returned time: %s " %item
        return item


def ObjectGenerator(maxlinenum):
    filename='/home/thinkit/Documents/usr_info/USER.csv'
    attributes=[]
    linenum=1
    a=UserInfo()
    file=open(filename)
    while linenum < maxlinenum:
        values=[]
        line=str.decode(file.readline(),'gb2312')#linecache.getline(filename, linenum,'gb2312')
        if line=='':
            print('reading fail! Please check filename!')
            break
        str_list=line.split(',')
        for item in str_list:
            item=item.strip()
            item=item.strip('\"')
            item=item.strip('\'')
            item=item.strip('+0*')
            item=catchTime(item)
            if linenum==1:
                attributes.append(item)
            else:
                values.append(item)
        if linenum==1:
            a.updateAttributes(attributes)
        else:
            a.updatePairs(values)
            yield a.attrilist #change to ' a ' to use
        linenum = linenum +1

if __name__ == '__main__':
    for n in ObjectGenerator(10):
        print(n)     #输出字典，看是否正确