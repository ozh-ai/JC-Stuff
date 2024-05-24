#Task 4.1
def initialise():
    suduku = [[4,3,2,1],[1,2,4,3],[3,4,1,2],[2,1,3,4]]
    return suduku

#Task 4.2
def display(suduku):
    for i in range(len(suduku)):
        for j in range(4):
            print(suduku[i][j],end=' ')
        print('')

def t1(suduku): #transformation 1
    quadrant = random.randint(1,2)
    if quadrant==1: #swap first 2 rows
        suduku[0],suduku[1] = suduku[1],suduku[0]
    else: #swap last 2 rows
        suduku[2],suduku[3] = suduku[3],suduku[2]

def t2(suduku): #Transformation 2
    quadrant = random.randint(1,2)
    if quadrant==1: #swap first 2 columns
        for i in range(len(suduku)):
            suduku[i][0],suduku[i][1] = suduku[i][1],suduku[i][0]
    else: #swap last 2 columns
        for i in range(len(suduku)):
            suduku[i][2],suduku[i][3] = suduku[i][3],suduku[i][2]

def t3(suduku): #Transformation 3
    suduku[0],suduku[2] = suduku[2],suduku[0] #swap 1st and 3rd rows
    suduku[1],suduku[3] = suduku[3],suduku[1] #swap 2nd and 4th rows
    
def t4(suduku): #Transformation 4
    for i in range(len(suduku)):
        suduku[i][0],suduku[i][2] = suduku[i][2],suduku[i][0] #swap 1st and 3rd columns
        suduku[i][1],suduku[i][3] = suduku[i][3],suduku[i][1] #swap 2nd and 4th columns

suduku = initialise()
display(suduku)

import random
transform1 = random.randint(1,4)
transform2 = random.randint(1,4)
while transform2==transform1:
    transform2 = random.randint(1,4) #decide on transformation 1 and 2
if transform1==1:
    t1(suduku)
elif transform1==2:
    t2(suduku)
elif transform1==3:
    t3(suduku)
else:
    t4(suduku)

if transform2==1:
    t1(suduku)
elif transform2==2:
    t2(suduku)
elif transform2==3:
    t3(suduku)
else:
    t4(suduku)

print("")
display(suduku)

