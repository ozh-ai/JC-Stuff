#2.1
##file = open('KEYS2.txt','r')
##numbers = []
##for line in file:
##    numbers.append(line.strip())
##ht = []
##for i in range(20):
##    ht.append('')
##for i in range(len(numbers)):
##    addr = int(numbers[i]) % 20
##    ht[addr] = numbers[i]
##print("{:^10}|{:^10}".format('Address','Number'))
##for i in range(20):
##    print("{:^10}|{:^10}".format(i,ht[i]))

#2.2
file = open('KEYS2.txt','r') #initialise both lists
numbers = []
for line in file:
    numbers.append(line.strip())
ht = []
for i in range(20):
    ht.append('')

for i in range(len(numbers)): #append ht
    addr = int(numbers[i]) % 20
    while ht[addr].isdigit() == True:
        addr = addr +1
        if addr > 19:
            addr = addr - 20
    ht[addr] = numbers[i]

print("{:^10}|{:^10}".format('Address','Number'))
for i in range(20):
    print("{:^10}|{:^10}".format(i,ht[i]))

#2.3
search = input("Enter ID number:")
for i in range(20):
    if search == ht[i]:
        print(i)
