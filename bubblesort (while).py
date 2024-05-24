def bubblesort(alist):
    i = len(alist)
    elements_switched = True
    while elements_switched==True and i>=2:
        j = 0
        elements_switched = False
        while j <= i-2:
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
                elements_switched = True
            j = j + 1
        i = i - 1
    return alist


print(bubblesort([6,5,4,3,2,1]))


    
