class Hashtable:
    def __init__(self,limit=11): 
        self.__limit = limit
        self.__data = [None for i in range(self.__limit)]

    def hashfunction(self,keydata): #function (modular)
        total = 0
        for each in keydata: #for i in range(len(keydata)): total = total + ord(keydata[i])
            total = total + ord(each) #convert character to ASCII number, chr converts ASCII number to character
        return total % self.__limit # % gives the remainder after division

    def rehash(self,oldhashvalue):
        return (oldhashvalue+1) % self.__limit #hashvalue +1

    def put(self,data): #add
        hashvalue = self.hashfunction(data) #calculate hash value (index of array)
        if (self.__data[hashvalue] == None) or (self.__data[hashvalue] == "DELETED"):
            self.__data[hashvalue] = data
        else: #collision!
            nextslot = self.rehash(hashvalue) #find the next slot
            while (self.__data[nextslot] != None) and (self.__data[nextslot] != "DELETED"):
                nextslot = self.rehash(nextslot)
            self.__data[nextslot] = data

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
    h1 = Hashtable(7)
    h1.put("apple")
    h1.put("orange")
    h1.put("durian") #if 2 of the data have the same index, the earlier one will be overwritten
    h1.display()
    h1.remove("durian")
    h1.display()
main() 
            
        
        
