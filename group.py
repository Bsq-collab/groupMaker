#!/usr/bin/python
print "content-type: text/html\n"

import cgitb, cgi, random
cgitb.enable()
results = cgi.FieldStorage()

#Class Roster
roster = {
    "Six": ["Abdullahnayeem","Angela","Anish","Bayan","Blythe","Brian","Charlotte","Datian","David","Emily","Irene","Jenny","Jonathan","Kaia","Kenneth","Kent","Lorenzo","Lydia","Matthew","Max","Maya","Mohamed T","Mohammad N","Nusheen","Oskar","Sarah","Rachel","Sakib","Shaikh","Sienna","Taylor","Yiduo","Yousuf","Zachary"],
    "Eight": ["Andre","Calvin","Cynthia","Daniel","David","Eli","Eric","Garrett","Gilvir","Ginevra","Isaac","Jacopo","Justin","Kai Hei","Kelly","Kevin","Leila","Megan","Michelle","Mika","Minseo","Nicholas","Pacy","Rochelle","Sammi","Sarah","Pallab","Simon","Sofiya","Stefan","Stephanie","Tahseen","Tiffany","Vicky"]
}

period = results.getvalue("period")

def startPage(title):
    return "<!DOCTYPE html>\n<html>\n  <head>\n    <meta charset=\"utf-8\">\n    <title>" + title +"</title>\n  </head>\n  <body>"

print startPage("Groups for Period %s" % period)

num_groups = 6
students = roster[period]

absentees = results.keys()
absentees.remove("period")

for absentee in absentees:
    students.remove(absentee)

groups = []
for i in range(num_groups):
    groups.append([])
random.shuffle(students)
for i in range(len(students)):
    groups[i%num_groups].append(students.pop())

print "    <h3>Groups for Period %s</h3>" % period

i = 0
while i < len(groups):
    print "    Group %d:" % (i+1), ", ".join(str(x) for x in groups[i])
    print "    <br><br>"
    i+=1

print "  </body>\n</html>"
