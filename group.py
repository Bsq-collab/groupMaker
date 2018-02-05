import random
students=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

one=[]
two=[]
three=[]
four=[]
five=[]
six=[]
def makeGroups(numOfGroups, students):
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
makeGroups(6,students)

print "one: "
print one
print "two: "
print  two
print "three: "
print three
print "four: "
print four
print "five: "
print five
print "six: "
print six
