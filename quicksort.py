def quicksort(arr):
    quicksorthelper(arr,0,len(arr)-1) #(arr,first,last)
    return arr

def quicksorthelper(arr,first,last):
    if first<last: #run until meet with one element
        splitpoint = partition(arr,first,last)
        quicksorthelper(arr,first,splitpoint-1)
        quicksorthelper(arr,splitpoint+1,last)

def partition(arr,first,last):
    pivot = arr[first] #set pivot to first value in arr
    left = first+1
    right = last

    done = False
    while done==False:
        while left<=right and arr[left]<=pivot:
            left = left+1
        while right>=left and arr[right]>=pivot:
            right = right-1
        if right<left:
            done = True
        else:
            arr[left],arr[right] = arr[right],arr[left]
    arr[first],arr[right] = arr[right],arr[first]
    return right

print(quicksort([9,5,6,7,4,8,3,2,1]))
print(quicksort([1,100,120,1203,39,2930,37,238,89]))
