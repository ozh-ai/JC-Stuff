#4.1
maze = []
file = open('MAZE.txt','r')
for line in file:
    maze.append(line.strip().split('\n'))
file.close()
##print(maze)

for i in range(11):
    maze[i][0] = maze[i][0].replace('P','.')

##for i in range(11):
##    for j in range(10):
##        print(maze[i][0][j]+" ",end="")
##    print()
##print()

#4.2
import random
placed = False
while placed == False:
    x = random.randint(0,9)
    y = random.randint(0,10)
    if maze[y][0][x] == '.':
        list1 = list(maze[y][0])
        list1[x] = 'P'
        maze[y][0] = ''
        for i in range(len(list1)):
            maze[y][0] = maze[y][0] + list1[i]
        placed = True

for i in range(11):
    for j in range(10):
        print(maze[i][0][j]+" ",end="")
    print()
print()

#4.3
def place(item,x,y):
    global maze
    placed = False
    while placed == False:
        if maze[y][0][x] == '.':
            list1 = list(maze[y][0])
            list1[x] = item
            maze[y][0] = ''
            for i in range(len(list1)):
                maze[y][0] = maze[y][0] + list1[i]
            placed = True

def clear(item,gone):
    global maze
    for i in range(11):
        maze[i][0] = maze[i][0].replace(item,gone)

win = False
previous = ''
while win == False:
    direction = input("Enter direction (U,D,L,R, ):")
    for i in range(11):
        for j in range(10):
            if maze[i][0][j] == 'O':
                y = i
                x = j

    if direction.upper() == '':
        direction = previous
            
    if direction.upper() == 'U':
        if maze[y-1][0][x] == '.':
            clear('O','.')
            y = y-1
            place('O',x,y)
        elif maze[y-1][0][x] == 'P':
            win = True
            clear('O','.')
            clear('P','.')
            y = y-1
            place('O',x,y)
        else:
            print("INVALID DIRECTION")
    elif direction.upper() == 'D':
        if maze[y+1][0][x] == '.':
            clear('O','.')
            y = y+1
            place('O',x,y)
        elif maze[y+1][0][x] == 'P':
            win = True
            clear('O','.')
            clear('P','.')
            y = y+1
            place('O',x,y)
        else:
            print("INVALID DIRECTION")
    elif direction.upper() == 'L':
        if maze[y][0][x-1] == '.':
            clear('O','.')
            x = x-1
            place('O',x,y)
        elif maze[y][0][x-1] == 'P':
            win = True
            clear('O','.')
            clear('P','.')
            x = x-1
            place('O',x,y)
        else:
            print("INVALID DIRECTION")
    elif direction.upper() == 'R':
        if maze[y][0][x+1] == '.':
            clear('O','.')
            x = x+1
            place('O',x,y)
        elif maze[y][0][x+1] == 'P':
            win = True
            clear('O','.')
            clear('P','.')
            x = x+1
            place('O',x,y)
        else:
            print("INVALID DIRECTION")
    previous = direction
        
    print()
    for i in range(11):
        for j in range(10):
            print(maze[i][0][j]+" ",end="")
        print()
    print()

print("You win! :)")

    



        
    
