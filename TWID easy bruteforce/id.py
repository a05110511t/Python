#!/usr/bin/python
# coding=utf-8
import sys, string, re
count = 0
def check(i): #check ID
    global count
    i = i.capitalize()
    if not re.match('^[A-Z][12][0-9]{8}$', i): 
        print 'GG';
    a = []; 
    a.extend("10987654932210898765431320")
    c = int(a[ord(i[0])-65]) + int(i[9])
    for x in range(1, 9): 
        c += int(i[x]) * (9 - x)
    if c % 10 == 0: 
        print count+1, "可能:", i
        count = count + 1
print "原本:", 'T120xxx517'
print "------------------"
for i in xrange(999):
    ID = 'T120'
    ID += ''.join(["{0:03}".format(i)]) #generate 000~999
    ID += '517'
    check(ID)
print "共有",count,"個可能"   
