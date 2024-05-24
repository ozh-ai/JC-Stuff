#3.1
class ToDo:
    def __init__(self,category,description): #constructor
        self.__category = category
        self.__description = description

    def getcategory(self):
        return self.__category
    def getdescription(self):
        return self.__description
    def setcategory(self,category):
        self.__category = category
    def setdescription(self,description):
        self.__description = description

    def summary(self):
        print("Category:",self.__category,"\nDescription:",self.__description,'\n')

    #3.2
    def comparewith(self,td):
        if self.getcategory() < td.getcategory():
            return -1
        elif self.getcategory() > td.getcategory():
            return 1
        else:
            if self.getdescription() < td.getdescription():
                return -1
            elif self.getdescription() > td.getdescription():
                return 1
            else:
                return 0

tasks = [ToDo("reading", "Try some Shakespeare"),\
         ToDo("shopping", "Consider items to recycle"),\
         ToDo("reading", "Search on the web"),\
         ToDo("reading", "Go to the library")]

tasklist = []
for i in range(len(tasks)):
    if len(tasklist) == 0:
        tasklist.append(tasks[i])
    else:
        current = 0
        while current<len(tasklist) and tasklist[current].comparewith(tasks[i])==-1:
            current = current+1
        if current == 0: #insert as first item
            tasklist.insert(0,tasks[i])
        elif tasklist[current-1].comparewith(tasks[i]) == 1:
            tasklist.insert(current-1,tasks[i])
        else: #0 or -1
            tasklist.insert(current, tasks[i]) #insert(position,object)

for i in range(len(tasks)):
    tasklist[i].summary()

#3.3
for eachtask in tasks:
    if len(tasklist) == 0:
        pass
