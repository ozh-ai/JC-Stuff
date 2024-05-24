#Task 4.1
def push(item):
    global stack
    stack.append(item)

def pop():
    global stack
    return stack.pop()

def size():
    global stack
    return len(stack)

#Task 4.2
def check(exp):
    opening = ['(','[','{']
    closing = [')',']','}']
    for i in range(len(exp)):
        if exp[i] in opening:
            push(exp[i])
        if i == len(exp)-1: #check for last symbol
            if exp[i] not in closing and len(stack)!=0:
                return "ERROR: too many opening symbols"
        if exp[i] in closing:
            size1 = size()
            if size1 == 0:
                return "ERROR: stack is empty"
            else:
                top = pop()
                if closing.index(exp[i]) != opening.index(top):
                    return "ERROR: symbols not matching"
    return "SUCCESS"
                
stack = []
print(check('8/4+4*5')) #Case where there is absence of brackets
stack = []
print(check('{8/[4+3*(6*7)4]*5}')) #Case where there is all 3 brackets used
stack = []
print(check('(8+8')) #Case where there is absence of corresponding closing bracket
stack = []
print(check('8+8)')) #Case where there is absence of opeing symbol
stack = []
print(check(')8+8(')) #Case where it starts with a closing symbol

    


