#Task 1.1
file = open('INVENTORY.txt','r') #read data from file
inventory = []
for line in file:
    inventory.append(line.strip())
file.close() #close the file

ItemTypes = []
for i in range(len(inventory)):
    if inventory[i] not in ItemTypes:
        ItemTypes.append(inventory[i])

ItemCounts = []
for i in range(len(ItemTypes)):
    count = 0
    for j in range(len(inventory)):
        if ItemTypes[i] == inventory[j]:
            count = count + 1
    ItemCounts.append(count)

print("{:^20}|{:^10}".format('ItemType','Count'))
print('')
for i in range(len(ItemTypes)):
    print("{:^20}|{:^10}".format(ItemTypes[i],ItemCounts[i]))

    

