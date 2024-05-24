#Task 1.1
def readfile():
    filename = input("Enter file name:") #read data from file
    file = open(filename,'r')
    data = []
    for line in file:
        data.append(line.strip())
    return data

def bubblesort(arr):
    compare = 0
    NoSwaps = False
    while NoSwaps == False:
        NoSwaps = True
        for i in range(0,len(arr)-1):
            compare = compare+1
            if arr[i] > arr[i+1]:
                NoSwaps = False
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr,compare

def insertionsort(arr):
    compare = 0
    for i in range(len(arr)):
        if arr[i] < arr[i-1]:
            temp = arr[i]
            j = i
            while j!=0 and temp<arr[j-1]:
                compare = compare+1
                arr[j] = arr[j-1]
                j = j - 1
            arr[j] = temp
    return arr,compare

def menu():
    print("1. Read file data\n2. Bubble sort\n3. Quick sort  / Insertion sort\n4. End")

#Task 1.2
menu()
end = False
while end == False:
    data = [5,4,3,2,1]
    option = input("Enter option:")
    if option == '1':
        data = readfile()
    if option == '2':
        sortedlist,comparisons = bubblesort(data)
        print(sortedlist)
        print(comparisons)
    if option == '3':
        sortedlist,comparisons = insertionsort(data) #sort method is insertion
        print(sortedlist)
        print(comparisons)
    if option == '4':
        end == True

    
    




