#3.1
class HashTable:
    def __init__(self,name,num):
        self.__name = name
        self.__num = num

    def getname(self):
        return self.__name
    def getnum(self):
        return self.__num
    def setname(self,name):
        self.__name = name
    def setnum(self,num):
        self.__num = num

    def displayvalues(self):
        print("{:^5}|{:^25}|{:^25}".format('INDEX','NAME','NUMBER'))
        for i in range(len(ht)):
            print("{:^5}|{:^25}|{:^25}".format(i,ht[i].getname(),ht[i].getnum()))

    #3.3
    def hashfn(self,searchname):
        hashtotal = 0
        for i in range(len(searchname)):
            asci = ord(searchname[i])
            result = asci*(i+1)
            hashtotal = hashtotal + result
        return hashtotal%500

    #3.4
    def search(self,searchname):
        hash1 = ht[0].hashfn(searchname)

        searched,giveup = False,False
        while searched==False and giveup==False:
            if ht[hash1].getname() == searchname:
                searched = True
            elif ht[hash1].getname() == '':
                giveup = True
            else:
                hash1 = hash1+1
        if searched == True:
            string = str(hash1) + ',' + ht[hash1].getname() + ',' + ht[hash1].getnum()
            return string
        else:
            return 'NOT FOUND'
            
ht = [HashTable('','') for i in range(500)]

#3.2
data = []
file = open('HASHEDDATA.txt','r')
for line in file:
    data.append(line.strip())
file.close()

data1 = []
for i in range(len(data)):
    if data[i][-1].isdigit() == True:
        data1.append(data[i])

for i in range(len(data1)):
    indiv = []
    indiv.append(data1[i].strip().split(','))
    indiv = indiv[0]
    ht[int(indiv[0])] = HashTable(indiv[1],indiv[2])
ht[0].displayvalues() #Why cannot ht.displayvalues() ?

searchname = input("Enter name to be searched:")
##print(ht[0].hashfn(searchname))

print(ht[0].search(searchname))

        
        
    
