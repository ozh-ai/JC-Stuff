#Task 2.1
class Node:
    def __init__(self,data,left=0,right=0):
        self.__data = data
        self.__left = left
        self.__right = right

    def getdata(self):
        return self.__data
    def getleft(self):
        return self.__left
    def getright(self):
        return self.__right
    def setleft(self,left):
        self.__left = left
    def setright(self,right):
        self.__right = right

#Task 2.2
filename = input("Enter file name:")
file = open(filename,'r')
keylist = []
keydict = {}
for line in file:
    keylist.append(line)
for i in range(len(keylist)):
    for j in range(len(keylist[i])):
        if keylist[i][j] not in keydict:
            keydict[keylist[i][j]] = 1
        else:
            value = keydict[keylist[i][j]] + 1
            keydict[keylist[i][j]] = value
file.close()

print(keydict)
tree = []
freq = 1
while freq<100:
    for each in keydict:
        if keydict[each]==freq:
            tree.append(Node(each))
    freq += 1
#Task 2.3 
for j in range(len(tree)):
    for i in range(len(tree)):
        if keydict[tree[i].getdata()] <= keydict[tree[i+2].getdata()]: #combine i and i+1
            tree.append(Node(tree[i].getdata()+tree[i+1].getdata(),i+1,i))
            keydict[tree[i].getdata()+tree[i+1].getdata()] = keydict[tree[i].getdata()]+keydict[tree[i+1].getdata()]
        else: #combine i+1 and i+2
            tree.append(Node(tree[i+1].getdata()+tree[i+2].getdata(),i+2,i+1))
            keydict[tree[i+1].getdata()+tree[i+2].getdata()] = keydict[tree[i+1].getdata()]+keydict[tree[i+2].getdata()]
        
        
            

