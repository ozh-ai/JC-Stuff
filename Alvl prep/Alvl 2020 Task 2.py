#Task 2.1
def task2_1(filename,quantity,maximum):
    file = open(filename,'w')
    import random
    for i in range(quantity):
        file.write(str(random.randint(0,maximum)))
        file.write('\n')
    file.close()

##task2_1('randomnumbers.txt',1000,5000)

#Task 2.2
def mergesort(A):
    if len(A) == 1:
        return A
    mid = len(A)//2
    left = [0 for i in range(mid)]
    right = [0 for i in range(mid,len(A))]
    for i in range(mid):
        left[i] = A[i]
    for i in range(mid,len(A)):
        right[i-mid] = A[i]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left,right)

def merge(L,R):
    A = [0 for i in range(len(L) + len(R))] #initialise array
    i,j,k = 0,0,0
    while i<len(L) and j<len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k  = k + 1
    while i<len(L):
        A[k] = L[i]
        i = i+1
        k = k+1
    while j<len(R):
        A[k] = R[j]
        j = j+1
        k = k+1
    return A
    
def task2_2(listofintegers):
    return mergesort(listofintegers)
    
print(task2_2([56,25,4,98,0,18,4,5,7,0]))
            
#Task 2.3
def task2_3(filename_in,filename_out):
    file = open(filename_in,'r')
    integers = []
    for line in file:
        integers.append(int(line.strip()))
    file.close()
    sortedlist = task2_2(integers)

    file = open(filename_out,'w')
    for i in range(len(sortedlist)):
        file.write(str(sortedlist[i]))
        file.write('\n')
    file.close()

task2_3('randomnumbers.txt','sortednumbers.txt')

    
        
            
    

    
