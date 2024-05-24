#2.1
'''A: value not in array'''
'''B: (low + high)/2'''
'''C: return binarysearch(array,value,middle+1,high)'''

#2.2
def initanimals(array):
    animal = input("Enter animal name:")
    high = len(array)
    low = 0
    print(binarysearch(array,animal,low,high))

def binarysearch(array,value,low,high):
    global count
    count = count + 1
    if value not in array:
        return 'Not found'
    else:
        mid = (low + high)//2
        if array[mid]>value:
            return binarysearch(array,value,low,mid-1)
        else:
            if array[mid]<value:
                return binarysearch(array,value,mid+1,high)
            else:
                return str(mid)+', count:'+str(count) #found at position middle

file = open('ANIMALS.txt','r')
list1 = []
for line in file:
    list1.append(line.strip().split('='))
file.close()

count = 0 #2.3
array = []
for i in range(len(list1)):
    list1[i].pop(0)
    array.append(list1[i][0])
    array[i] = array[i].replace('"','')
initanimals(array)
    
