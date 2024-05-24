#4.1
'''Use a 2d array to define the pond, 8 rows by 15 columns, x from 1 to 15, y from 1 to 8.
top left corner is 1,1
Contents: Use . to represent water in the pond, S to represent the stone that has been thrown
function declarepond used to define array
function display takes the 2d array and display it as a grid'''

def declarepond():
    pond = [['.' for i in range(15)] for j in range(8)]
    return pond

def display(pond):
    print("")
    for i in range(len(pond)):
        for j in range(len(pond[i])):
            print(pond[i][j], end='')
        print()

def throw(pond):
    x = eval(input("Enter x coordinate <1 to 15> :"))
    y = eval(input("Enter y coordinate <1 to 8> :"))
    pond[y-1][x-1] = 'S'

#4.2
pond = declarepond()
##throw(pond)
##display(pond)

#4.3
##import random
##fishx = []
##fishy = []
##for i in range(3):
##    x = random.randint(1,15)
##    y = random.randint(1,8)
##    fishx.append(x)
##    fishy.append(y)
##
##for i in range(len(fishx)):
##    pond[fishy[i]][fishx[i]] = 'F'
##display(pond)

#4.4
import random
def fish(n):
    for i in range(n):
        x = random.randint(1,15)-1
        y = random.randint(1,8)-1
        if pond[y][x]=='F' or pond[y][x]=='H':
            n = n+1
        else:
            pond[y][x] = 'F'
    for i in range(3-n):
        if pond[y][x]=='F' or pond[y][x]=='H':
            n = n+1
        else:
            pond[y][x] = 'H'

n = 3
while True:
    fish(n)
    x = eval(input("Enter x coordinate <1 to 15> :"))
    y = eval(input("Enter y coordinate <1 to 8> :"))
    if pond[y-1][x-1] == '.':
        pond[y-1][x-1] = 'P'
    elif pond[y-1][x-1] == 'F':
        pond[y-1][x-1] = 'H'
        n = n-1
    else:
        pass
    display(pond)
    pond = declarepond()
    
    
    
    

    


