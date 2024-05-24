#3.2
class listnode:
    def __init__(self,data='',pointer=0): #initialise, constructor
        self.__data = data
        self.__pointer = pointer

    def getdata(self):
        return self.__data
    def setdata(self,data):
        self.__data = data
    def getpointer(self):
        return self.__pointer
    def setpointer(self,pointer):
        self.__pointer = pointer

class linkedlist:
    def __init__(self):
        self.__node = [None] + [listnode() for i in range(30)]
        for i in range(1,30):
            self.__node[i].setpointer(i+1)
        self.__start = 0
        self.__nextfree = 1

    def AddNode(self): #3.4
        newitem = input("Enter item to be added:")
        self.__node[self.__nextfree].setdata(newitem)

        if self.__start == 0:
            self.__start = self.__nextfree
            temp = self.__node[self.__nextfree].getpointer()
            self.__node[self.__nextfree].setpointer(0)
            self.__nextfree = temp
            print(self.__start)
            print(self.__node[self.__start].getdata())
        else:
            #traverse the list - starting at start to find the position to insert new item
            temp = self.__node[self.__nextfree].getpointer()

            if newitem < self.__node[self.__start].getdata():
                #newitem will become the start of the list
                self.__node[self.__nextfree].setpointer(self.__start)
                self.__start = self.__nextfree
                self.__nextfree = temp
            else:
                #the newitem is not at start of the list
                previous = 0
                current = self.__start
                found = False

                while found==False and current!=0:
                    if newitem <= self.__node[current].getdata():
                        self.__node[previous].setpointer(self.__nextfree) 
                        self.__node[self.__nextfree].setpointer(current)
                        self.__nextfree = temp
                        found = True
                    else:
                        #move on to next node
                        previous = current
                        current = self.__node[current].getpointer()

                if current == 0:
                    self.__node[previous].setpointer(self.__nextfree)
                    self.__node[self.__nextfree].setpointer(0)
                    self.__nextfree = temp

    def TraversalInOrder(self,index):
        if index != 0:
            print(self.__node[index].getdata())
            #follow the pointer to the next data item in the linked list
            self.TraversalInOrder(self.__node[index].getpointer())
            
    def Traversal(self):
        self.TraversalInOrder(self.__start)

    def TraversalInReverseOrder(self,index):
        if index != 0:
            self.TraversalInReverseOrder(self.__node[index].getpointer())
            print(self.__node[index].getdata())

    def RevTraversal(self):
        self.TraversalInReverseOrder(self.__start)

    def display(self):
        print(self.__start)
        print("|{:^10}|{:^10}|{:^10}|".format('INDEX','DATA','POINTER'))
        for i in range(29):
            print("|{:^10}|{:^10}|{:^10}|".format(i+1,self.__node[i+1].getdata(),self.__node[i+1].getpointer()))

    def isempty():
        return self.__start == 0 #start will point at 0 (NULL) when empty linked

    def isfull():
        return self.__nextfree == 0

#3.1
LL = linkedlist()
out = False
while out == False:
    print("~"*50)
    print("MENU\n1. Add an item\n2.Traverse the linked list of used nodes and output the data values\n3.Output all pointers and data values\n4. Taverse the linked list in reverse order\n5. Exit")
    print("~"*50)
    print()

    choice = input("Enter option:")
    if choice == '1':
        LL.AddNode()
    elif choice == '2':
        LL.Traversal()
    elif choice == '3': #3.3
        LL.display()
    elif choice == '4':
        LL.RevTraversal()
    elif choice == '5':
        out = True
    else:
        print("Invalid option")

