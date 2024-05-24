#TASK 1
Max = 20
file = open("KEYS2.txt","r") #KEYS2.txt for Task 2
numbers = []
for line in file:
    numbers.append(line.strip())
file.close()
hashtable = [None for i in range(Max)]
for i in range(len(numbers)):
    address = int(numbers[i]) % Max
    while hashtable[address] != None:
        
    



#TASK 3
IDnumber = input("Enter ID number to search:")
while not IDnumber.isdigit():
    print("You did not enter a valid ID number. \n")
    IDnumber = input("Enter ID number to search:")
address = int(IDnumber) % Max #get address
while hashtable[address] != 
