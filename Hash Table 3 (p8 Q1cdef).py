class CreateHashTable:
    def __init__(self,limit=9): 
        self.__limit = limit
        self.__data = ["[" "," "]" for i in range(self.__limit)]

    def hashfunction(self,keydata): #function (modular)
        total = 0
        for each in keydata: #for i in range(len(keydata)): total = total + ord(keydata[i])
            total = total + ord(each) #convert character to ASCII number, chr converts ASCII number to character
        return total % self.__limit # % gives the remainder after division

    def rehash(self,oldhashvalue):
        return (oldhashvalue+1) % self.__limit #hashvalue +1

    def addrecord(filename):
        file = open(customers.txt,"r")
        for line in file:
            ID, Name = line[:-1].split(',')
            hashcode = hashfunction(ID)
            if len()

    def remove(self,data):
        hashvalue = self.hashfunction(data) #calculate hash value (index of array)
        if self.__data[hashvalue] == data:
            self.__data[hashvalue] = "DELETED"
        else:
            nextslot = self.rehash(hashvalue) #find the next slot
            count = 0
            while (self.__data[nextslot] != data) and (count != self.__limit):
                nextslot = self.rehash(nextslot)
                count = count + 1
            if count != self.__limit:
                self.__data[nextslot] = "DELETED"
            else:
                print(data, "not found")

    def display(self):
        print("")
        print("|{:^5}|{:^15}|".format("INDEX","DATA"))
        for i in range(self.__limit):
            print("|{:^5}|{:^15}|".format(i, str(self.__data[i])))

def main(): #driver program
    ht = CreateHashTable()
    ht.addrecord("customer.txt")
main() 
            
        
        
