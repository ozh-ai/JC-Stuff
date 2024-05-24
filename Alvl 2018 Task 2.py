#2.1
def quicksort(scores):
    qshelper(scores,0,len(scores)-1)
    return scores

def qshelper(scores,first,last):
    if first < last:
        splitpoint = partition(scores,first,last)
        qshelper(scores,first,splitpoint-1)
        qshelper(scores,splitpoint+1,last)
    return scores

def partition(scores,first,last):
    pivot = scores[first]
    left = first + 1
    right = last
    done = False
    while done == False:
        while left<=right and scores[left]<=pivot:
            left = left+1
        while scores[right]>=pivot and right>=left:
            right = right-1
        if right<left:
            done = True
        else:
            temp = scores[left]
            scores[left] = scores[right]
            scores[right] = temp
    scores[first],scores[right] = scores[right],scores[first]
    return right

#2.2
def output(scores):
    for i in range(len(scores)):
        print(scores[i],end=' ')
    print()
    
numbers = []
file = open('SCORES.txt','r')
for line in file:
    numbers.append(line.strip().split(','))
file.close()
numbers = numbers[0]
output(numbers)
output(quicksort(numbers))
    
        
