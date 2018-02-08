#!/usr/bin/python
print "content-type: text/html\n"

import cgitb
cgitb.enable()
import cgi
formresults = cgi.FieldStorage()

import random

#Roster for period 6:
students6=["abdullahnayeem","angela","anish","bayan","blythe","brian","charlotte","datian","david","emily","irene","jenny","jonathan","kaia","kenneth","kent","lorenzo","lydia","matthew","max","maya","mohamed t","mohammad n","nusheen","oskar","sarah","rachel","sakib","shaikh","sienna","taylor","yiduo","yousuf","zachary"]

#Roster for period 8
students8=["andre","calvin","cynthia","daniel","david","eli","eric","garrett","gilvir","ginevra","isaac","jacopo","justin","kai hei","kelly","kevin","leila","megan","michelle","mika","minseo","nicholas","pacy","rochelle","sammi","sarah","pallab","simon","sofiya","stefan","stephanie","tahseen","tiffany","vicky"]


#declaring the groups-- clears them at each run
one=[]
two=[]
three=[]
four=[]
five=[]
six=[]

def startPage(title):
    return "<!DOCTYPE html>\n <html>\n  <head>\n   <title>" + title +"</title>\n  </head>\n <body>\n"

print startPage("groups")


def getPeriod():
    '''returns the period number 6 or 8 to be used later'''
    period=input("What period is it(6 or 8)\n\n")
    if formresults.getvalue('period')=='six':
        students=absent(students6)
        makeGroups6(students6)
    elif formresults.getvalue('period')=='eight':
        students=absent(students8)
        makeGroups6(students8)
    
    
    #while period!=6 and period!=8:
       # period=input("Invalid try again\n\n")
 #   print "good period: "+ str(period)
#    return period;


def absent(students):

    ''' removes students from the array... spelling is important'''
    
    if formresults.getvalue('absentees'):
        absentees=formresults.getvalue('absentees').split(",")
        for each in absentees:
            students.remove(each.lower())
        
    '''
    ctr=1
    while(ctr<=numAbsent):
        nameOfAbsentee=raw_input("Name of absentee number "+str(ctr)+":\n\n")
        students.remove(nameOfAbsentee) #make sure you check the way i printed the roster above
        ctr+=1
'''
    return students

#Makes groups of six given 6 and students as a parameter
def makeGroups6( students):
    '''makes groups of 6'''
    ctr=1;
    index=0;
    random.shuffle(students)
    while(ctr<=6 and index<len(students)):
       if(ctr==1):
           one.append(students[index])
           ctr+=1
       elif(ctr==2):
           two.append(students[index])
           ctr+=1
       elif(ctr==3):
           three.append(students[index])
           ctr+=1
       elif(ctr==4):
           four.append(students[index])
           ctr+=1
       elif(ctr==5):
           five.append(students[index])
           ctr+=1
       elif(ctr==6):
           six.append(students[index])
           ctr=1
       index+=1

#makes groups of 5 given 5 and students as a parameter
def makeGroups5( students):
    ctr=1;
    index=0;
    random.shuffle(students)
    while(ctr<=5 and index<len(students)):
       if(ctr==1):
           one.append(students[index])
           ctr+=1
       elif(ctr==2):
           two.append(students[index])
           ctr+=1
       elif(ctr==3):
           three.append(students[index])
           ctr+=1
       elif(ctr==4):
           four.append(students[index])
           ctr+=1
       elif(ctr==5):
           five.append(students[index])
           ctr=1
       index+=1



'''period=getPeriod()

if(period==6):
    print"Here is the roster for period 6 if anyone's absent match the spelling the way i spelled it (ex: mohamed t)\n\n"
    print students6
    print"\n\n\n"
    students6=absent(students6)
    makeGroups6(students6)#if period 6 prefers 5 groups do: makeGroups5(students6)
elif(period==8):

    print"Here is the roster for period 6 if anyone's absent match the spelling the way i spelled it(ex: sarah c)\n\n"
    print students8
    print"\n\n\n"
    students8=absent(students8)
    makeGroups6(students8)#if period 8 prefers 5 groups do: makeGroups5(students8)
'''


if formresults.getvalue('period')=='six':
    students=absent(students6)
    makeGroups6(students6)
elif formresults.getvalue('period')=='eight':
    students=absent(students8)
    makeGroups6(students8)
print "\n\n6 GROUPS:<br>"
print "one: <br>"
print one
print "<br>two: <br>"
print  two
print "<br>three: <br>"
print three
print "<br>four:<br> "
print four
print "<br>five:<br>"
print five
print "<br>six:<br> "
print six
