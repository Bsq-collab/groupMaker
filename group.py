import random
#Roster for period 6:
students6=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8']
#Roster for period 8
students8=[]
#declaring the groups
one=[]
two=[]
three=[]
four=[]
five=[]
six=[]

#Makes groups of six given 6 and students as a parameter
def makeGroups6(numOfGroups, students):
    ctr=1;
    index=0;
    random.shuffle(students)
    while(ctr<=numOfGroups and index<len(students)):
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


def makeGroups5(numOfGroups, students):
    ctr=1;
    index=0;
    random.shuffle(students)
    while(ctr<=numOfGroups and index<len(students)):
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


makeGroups6(6,students6)
print "\n\n6 GROUPS:\n\n"
print "one: "
print one
print "\n\ntwo: "
print  two
print "\n\nthree: "
print three
print "\n\nfour: "
print four
print "\n\nfive: "
print five
print "\n\nsix: "
print six

#clearing
one=[]
two=[]
three=[]
four=[]
five=[]
six=[]

makeGroups5(5,students8)

print"\n\nFIVE GROUPS:\n\n"
print "one: "
print one
print "\n\ntwo: "
print  two
print "\n\nthree: "
print three
print "\n\nfour: "
print four
print "\n\nfive: "
print five
print "\n\nsix: "
print six
