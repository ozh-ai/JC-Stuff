Nullpointer = 0 #define constant value for nullpointer

class TreeNode:
    def __init__(self,data,left=0,right=0):
        self.__data = data
        self.__lp = left
        self.__rp = right

    def getdata(self):
        return self.__data
    def getlp(self):
        return self.__lp
    def getrp(self):
        return self.__rp
    def setdata(self,data):
        self.__data = data
    def setlp(self,lp):
        self.__lp = lp
    def setrp(self,rp):
        self.__rp = rp

class BST:
    def __init__(self,size=7):
        self.__tree = [None]+[TreeNode("") for i in range(size)] #None in base 0 so first tree node from index 1
        for i in range(1,size): #Index 1 to Index 6
            self.__tree[i].setlp(i+1)
        self.__tree[size].setlp(Nullpointer) #Let the last node (7th node) point to null (START FROM INDEX 1) 
        self.__Rootpointer = Nullpointer
        self.__FP = 1 #Start from node when BST is empty

    def display(self):
        print("{:^5}|{:^5}|{:^10}|{:^5}".format("INDEX","LP","DATA","RP"))
        for i in range(1,len(self.__tree)):
            print("{:^5}|{:^5}|{:^10}|{:^5}".format(i,self.__tree[i].getlp(),self.__tree[i].getdata(),self.__tree[i].getrp())) #print the contents
        print("Root pointer:",self.__Rootpointer)
        print("Free pointer:",self.__FP)

    def insertnode(self,newitem):
        if self.__FP != Nullpointer:
            NNP = self.__FP #NNP stands for newnodepointer
            self.__FP = self.__tree[self.__FP].getlp()
            self.__tree[NNP].setdata(newitem)
            self.__tree[NNP].setlp(Nullpointer)
            self.__tree[NNP].setrp(Nullpointer)

            if self.__Rootpointer == Nullpointer:
                self.__Rootpointer = NNP
            else:
                cur = self.__Rootpointer
                while cur != Nullpointer:
                    prev = cur
                    if newitem < self.__tree[cur].getdata():
                        turnedleft = True
                        cur = self.__tree[cur].getlp()
                    else:
                        turnedleft = False
                        cur = self.__tree[cur].getrp()
                if turnedleft == True:
                    self.__tree[prev].setlp(NNP)
                else:
                    self.__tree[prev].setrp(NNP)
        else:
            print("No free node available")

    def fill(self):
        import random
        for i in range(1,8):
            n = random.randint(1,10000000)
            self.insertnode(n)

    def findnode(self,searchitem):
        cur = self.__Rootpointer
        while cur != Nullpointer and self.__tree[cur].getdata() != searchitem:
            if searchitem < self.__tree[cur].getdata():
                cur = self.__tree[cur].getlp()
            else:
                cur = self.__tree[cur].getrp()
        return cur

    def Inorder(self,index): #traverse left, root, right
        if index != Nullpointer:
            self.Inorder(self.__tree[index].getlp())
            print(self.__tree[index].getdata())
            self.Inorder(self.__tree[index].getrp())

    def Preorder(self,index): #traverse root, left, right
        if index != Nullpointer:
            print(self.__tree[index].getdata())
            self.Preorder(self.__tree[index].getlp())
            self.Preorder(self.__tree[index].getrp())

    def Postorder(self,index): #traverse left, right, root
        if index != Nullpointer:
            self.Postorder(self.__tree[index].getlp())
            self.Postorder(self.__tree[index].getrp())
            print(self.__tree[index].getdata())

    def getRootpointer(self):
        return self.__Rootpointer

def main(): #driver program
    bst = BST()
    bst.insertnode("Durian")
    bst.insertnode("Orange")
    bst.insertnode("Apple")
    bst.insertnode("Honeydew")
    bst.insertnode("Banana")
    bst.display()
    bst.Inorder(bst.getRootpointer()) #bst.Inorder(bst.__RootPointer) ##error access: private attribute
main()
    
        
  
        
            

                        
            
            
            
