#Task 1.1
file = open('TIDES.txt','r')
tide = []
for line in file:
    tide.append(line.strip().split('\t'))

highest = float(tide[0][3])
for i in range(len(tide)):
    if float(tide[i][3]) > highest:
        highest = float(tide[i][3])
print(highest)

lowest = float(tide[0][3])
for i in range(len(tide)):
    if float(tide[i][3]) < lowest:
        lowest = float(tide[i][3])
print(lowest)
print()

#Task 1.2
if float(tide[0][3]) - float(tide[1][3]) >= 0: #Use abs
    largest = float(tide[0][3]) - float(tide[1][3])
    smallest = float(tide[0][3]) - float(tide[1][3])
else:
    largest = float(tide[1][3]) - float(tide[0][3])
    smallest = float(tide[1][3]) - float(tide[0][3])
smalldate, largedate = tide[1][0], tide[1][0]
    
for i in range(len(tide) - 1):
    if float(tide[i][3]) - float(tide[i+1][3]) >= 0:
        tr = float(tide[i][3]) - float(tide[i+1][3])
    else:
        tr = float(tide[i+1][3]) - float(tide[i][3])
    
    if tr > largest:
        largest = tr
        largedate = tide[i+1][0]
    elif tr < smallest:
        smallest = tr
        smalldate = tide[i+1][0]

print(largest)
print(largedate)
print()
print(smallest)
print(smalldate)


    
    
