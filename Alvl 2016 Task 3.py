#Task 3.1
class Node:
    def __init__(self,index,data,LP,RP):
        self.__index = index
        self.__data = data
        self.__LP = LP
        self.__RP = RP

    def getindex(self):
        return self.__index
    def getdata(self):
        return self.__data
    def getLP(self):
        return self.__LP
    def getRP(self):
        return self.__RP
    def setdata(self,data):
        self.__data = data
    def setLP(self,LP):
        self.__LP = LP
    def setRP(self,RP):
        self.__RP = RP

class Tree:
    def __init__(self):
        self.__tree = [None]+[Node(i+1,'',i+2,0) for i in range(20)]
        self.__tree[20] = Node(20,'',0,0)
        self.__root = 0
        self.__FP = 1

    def add(self,data):
        if self.__FP!=0:
            newnode = self.__FP
            self.__FP = self.__tree[self.__FP].getLP() #nextfree point to new node
            self.__tree[newnode].setdata(data) #insert data into node
            self.__tree[newnode].setLP(0)
            self.__tree[newnode].setRP(0)

            if self.__root==0: #if list is empty
                self.__root = newnode
            else: #traverse the bst to find right position
                current = self.__root
                while current!=0:
                    prev = current
                    if data<self.__tree[current].getdata():
                        turnedleft = True
                        current = self.__tree[current].getLP()
                    else:
                        turnedleft = False
                        current = self.__tree[current].getRP()

                if turnedleft == True:
                    self.__tree[prev].setLP(newnode)
                else:
                    self.__tree[prev].setRP(newnode)
        else:
            print("No free node available")            

    #Task 3.3
    def inorder(self,index):
        if index!=0:
            self.inorder(self.__tree[index].getLP())
            print(self.__tree[index].getdata())
            self.inorder(self.__tree[index].getRP())

    def findnode(self,searchitem):
        current = self.__root
        while current!=0 and self.__tree[current].getdata()!=searchitem:
            if searchitem<self.__tree[current].getdata():
                current = self.__tree[current].getLP()
            else:
                current = self.__tree[current].getRP()
        return current
                        
    def print(self):
        print("{:^5}|{:^5}|{:^10}|{:^5}".format('INDEX','LP','DATA','RP'))
        for i in range(1,len(self.__tree)):
            print("{:^5}|{:^5}|{:^10}|{:^5}".format(self.__tree[i].getindex(),self.__tree[i].getLP(),self.__tree[i].getdata(),self.__tree[i].getRP()))
        print("FP",self.__FP)
        print("Root:",self.__root)

#Task 3.2
Tree().print()
bst = Tree()
bst.add('Dave')
bst.add('Fred')
bst.add('Ed')
bst.add('Greg')
bst.add('Bob')
bst.add('Cid')
bst.add('Ali')
bst.print()
bst.inorder(1)
print(bst.findnode('Ali'))
        
                
    
            
        
        
        
        
