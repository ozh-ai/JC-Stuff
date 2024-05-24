#Task 3.1
class Node:
    def __init__(self,data,priority,Next):
        self.__data = data
        self.__priority = priority
        self.__Next = Next

    def getdata(self):
        return self.__data
    def getpriority(self):
        return self.__priority
    def getnext(self):
        return self.__Next
    def setdata(self,data):
        self.__data = data
    def setpriority(self,priority):
        self.__priority = priority
    def setnext(self,Next):
        self.__Next = Next 

class PQueue:
    def __init__(self):
        self.thisPQueue = [None]+[Node('','',i+2) for i in range(9)]
        self.thisPQueue.append(Node('','',0))
        self.__front = 0
        self.__rear = 0
        self.__NextFree = 1

    def PQinsert(self,newitem,priority):
        if self.__NextFree != 0:
            temp = self.__NextFree
            self.__NextFree = self.thisPQueue[self.__NextFree].getnext()
            self.thisPQueue[temp].setdata(newitem)
            self.thisPQueue[temp].setpriority(priority)
            self.thisPQueue[temp].setnext(0)

            if self.__front==0:
                self.__front = temp
            else:
                self.thisPQueue[self.__rear].setnext(temp)
            self.__rear = temp
        else:
            print("Queue is full!")

    def PQdelete(self):
        if self.__front==0:
            print("Queue is empty")
        else:
            highest = self.thisPQueue[1].getpriority() #search for highest priority
            index = 1
            for i in range(1,10):
                if self.thisPQueue[i].getpriority()!='' and int(self.thisPQueue[i].getpriority())>int(highest):
                    index = i
            prev = 0
            cur = self.__front
            while cur!=0 and cur!=index:
                prev = cur
                cur = self.thisPQueue[cur].getnext()
                if cur==0:
                    return 'empty list' 

            if cur == self.__front:
                self.__front = self.thisPQueue[cur].getnext()
            elif cur == self.__rear:
                self.thisPQueue[prev].setnext(0)
                self.__rear = prev
            else:
                self.thisPQueue[prev].setnext(self.thisPQueue[cur].getnext())
            data = self.thisPQueue[cur].getdata()
            self.thisPQueue[cur].setdata('')
            self.thisPQueue[cur].setpriority('')
            self.thisPQueue[cur].setnext(self.__NextFree)
            self.__NextFree = cur
            return data

    def displayPQueue(self):
        print("{:^10}|{:^20}|{:^20}|{:^20}".format('index','data','priority','Next'))
        for i in range(1,10):
            print("{:^10}|{:^20}|{:^20}|{:^20}".format(i,self.thisPQueue[i].getdata(),self.thisPQueue[i].getpriority(),self.thisPQueue[i].getnext()))
                
#Task 3.2
q = PQueue()
q.__init__()
file = open('PATIENTS.txt','r')
datalist = []
for line in file:
    datalist.append(line.strip().split(','))
file.close()
for i in range(len(datalist)):
    q.PQinsert(datalist[i][0],datalist[i][1])
q.displayPQueue()

#Task 3.3
q.PQdelete()
q.PQdelete()
q.PQinsert('Carol',4)
q.PQdelete()
q.PQdelete()
q.displayPQueue()



            
            
            

        
        
