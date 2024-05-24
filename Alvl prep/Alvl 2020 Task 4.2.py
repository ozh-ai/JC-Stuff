class Person:
    def __init__(self,fullname,DOB):
        self.__fullname = fullname
        self.__DOB = DOB

    def is_adult(self):
        age = 2021 - int(self.__DOB[0:3])
        if age > 18:
            return '1'
        else:
            return '0'

    def screen_name(self):
        screenname = ''
        for i in range(len(fullname)):
            if fullname[i] != ' ':
                screenname = screenname + self.__fullname[i]
        screenname = screenname + self.__DOB[5:6] + self.__DOB[8:9]
        return screenname

class Staff(Person):
    def __init__(self,fullname,DOB):
        super().__init__(fullname,DOB)
    
    def is_adult(self):
        return '0'
        
    def screen_name(self):
        screenname = ''
        for i in range(len(self.__fullname)):
            if fullname[i] != ' ':
                screenname = screenname + self.__fullname[i]
        screenname = screenname + DOB[5:6] + DOB[8:9] + '"Staff"'
        return screenname

class Student(Person):
    def __init__(self,fullname,DOB):
        super().__init__(fullname,DOB)
        
    def is_adult():
        return '0'

    def screen_name(fullname,DOB):
        screenname = ''
        for i in range(len(fullname)):
            if fullname[i] != ' ':
                screenname = screenname + fullname[i]
        screenname = screenname + DOB[5:6] + DOB[8:9] 
        return screenname

file = open('people.txt','r')
people = []
for line in file:
    people.append(line.strip().split(','))
file.close()

allinfo = []
for i in range(len(people)):
    if people[i][2] == 'Person':
        allinfo.append(Person(people[i][0],people[i][1]))
    if people[i][2] == 'Staff':
        allinfo.append(Staff(people[i][0],people[i][1]))
    if people[i][2] == 'Student':
        allinfo.append(Student(people[i][0],people[i][1]))

import sqlite3
db = sqlite3.connect('Alvl 2020 Task 4.db')

for data in people:
    db.execute("INSERT INTO People(FullName,DateOfBirth,ScreenName,IsAdult) VALUES(?,?,?,?)",\
               (data[0],data[1],Person.screen_name(),Person.is_adult()))
db.commit()
db.close()
    
        
        
