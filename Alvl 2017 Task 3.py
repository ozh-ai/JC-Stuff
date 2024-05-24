#Task 3.1
class ConnectionNode:
    def __init__(self,data,leftchild,rightchild):
        self.__data = data
        self.__leftchild = leftchild
        self.__rightchild = rightchild

    def getdata(self):
        return self.__data
    def getleftchild(self):
        return self.__leftchild
    def getrightchild(self):
        return self.__rightchild
    def setdata(self,data):
        self.__data = data
    def setleftchild(self,leftchild):
        self.__leftchild = leftchild
    def setrightchild(self,rightchild):
        self.__rightchild = rightchild

robotdata = [None]+[ConnectionNode('',i+1,0) for i in range(1,26)]
robotdata[25].setleftchild(0)
root = 1
nextfreechild = 1

#Task 3.2
def findnode(nodevalue):
    global root
    found = False
    current = root
    while found==False and current<=25:
        if robotdata[current].getdata()==nodevalue:
            found = True
        else:
            current = current+1
    if current>25:
        return 0
    else:
        return current

def add(newdata,parent,thismove):
    global root
    global nextfreechild
    if root==1 and nextfreechild==1:
        nextfreechild = robotdata[nextfreechild].getleftchild()
        robotdata[root].setleftchild(0)
        robotdata[root].setdata(newdata)
    else:
        parentposition = findnode(parent)
        if parentposition>0:
            existingchild = findnode(newdata)
            if existingchild>0:
                childpointer = existingchild
            else:
                childpointer = nextfreechild
                nextfreechild = robotdata[nextfreechild].getleftchild()
                robotdata[childpointer].setleftchild(0)
                robotdata[childpointer].setdata(newdata)
            if thismove=='L':
                robotdata[parentposition].setleftchild(childpointer)
            else:
                robotdata[parentposition].setrightchild(childpointer)

#Task 3.3
def outputdata():
    print("{:^5}|{:^10}|{:^10}|{:^10}".format('Index','Data','LeftChild','RightChild'))
    for i in range(1,26):
        print("{:^5}|{:^10}|{:^10}|{:^10}".format(i,robotdata[i].getdata(),robotdata[i].getleftchild(),robotdata[i].getrightchild()))
    print("Root:",root)
    print("NextFreeChild:",nextfreechild)
                        
file = open('SEARCHTREE.txt','r')
data = []
for line in file:
    data.append(line.strip().split(','))
file.close()

for i in range(len(data)):
    add(data[i][0],data[i][1],data[i][2])
outputdata()

        
    
        
