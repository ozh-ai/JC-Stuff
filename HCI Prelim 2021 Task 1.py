#Task 1.1
def quicksort(arr):
    quicksorthelper(arr,0,len(arr)-1)
    return arr

def quicksorthelper(arr,first,last):
    if first<last:
        splitpoint = partition(arr,first,last)
        quicksorthelper(arr,first,splitpoint-1)
        quicksorthelper(arr,splitpoint+1,last)

def partition(arr,first,last):
    pivot = arr[first]
    left = first+1
    right = last

    done = False
    while done==False:
        while left<=right and arr[left]<=pivot:
            left = left+1
        while left<=right and arr[right]>=pivot:
            right = right-1
        if left>right:
            done=True
        else:
            arr[left],arr[right] = arr[right],arr[left]
    arr[first],arr[right] = arr[right],arr[first]
    return right

#Task 1.2
def binarysearch(arr,target):
    if target not in arr:
        print('Target not found')
        return 0
    count = 0
    first = 0
    last = len(arr)-1
    mid = (first+last)//2
    while True:
        count = count+1
        if target<arr[mid]:
            last = mid-1
            mid = (first+last)//2
        elif target>arr[mid]:
            first = mid+1
            mid = (first+last)//2
        else:
            print("Target found")
            return count
        

file = open('INTEGERS.txt','r')
numbers = []
for line in file:
    numbers.append(line.strip())
file.close()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers = quicksort(numbers)

file = open('sortedlist.txt','w')
for i in range(len(numbers)):
    file.write(str(numbers[i])+'\n')
file.close()

print(binarysearch(numbers,172))

#Task 1.3
import random
randomnumbers=[]
for i in range(200):
    number = random.randint(1,200)
    randomnumbers.append(number)
totalcount = 0

for i in range(200):
    count = binarysearch(numbers,randomnumbers[i])
    totalcount = int(totalcount)+int(count)
average = totalcount/50
print("average:",average)




        
