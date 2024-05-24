#Task 1.1
names = []
steps = []
for i in range(10):
    name = input("Enter name:")
    while not name.isalpha():
        print("Invalid name")
        name = input("Enter name:")
    names.append(name)

    step = input("Enter number of steps:")
    while not step.isdigit() or int(step)<0 or int(step)>100000:
        print("Invalid step count")
        step = input("Enter number of steps:")
    steps.append(step)

    if i<9:
        more = input("Is there any more names? (Y/N) ")
        if more[0].upper() != 'Y':
            break
    print()

print(names)
print(steps)

high = 0
for i in range(len(steps)):
    if int(steps[i]) > high:
        high = int(steps[i])
        index = i

data = []
file = open('STAR.txt','r')
for line in file:
    data.append(line.strip().split(',')[-1])
file.close()

data.append(names[index])
data.append(steps[index])

file = open('STAR.txt','w')
for i in range(len(data)):
    if data[i].isdigit() == False:
        file.write(data[i]+'\n')
    else:
        file.write(','+data[i]+'\n')
file.close()

print("Last week,",data[-4][0],"was 'Star of the Week' with",data[-3][0],"steps taken.")
print("This week,",data[-2][0],"was 'Star of the Week' with",data[-1][0],"steps taken.")

#Task 1.2
#Test for boundary cases, normal cases, erronous cases(validate steps)
#Case 1: Test minimum of 1 value added
#Case 2: Test normal range of values between 1 and 10, eg. 5 values added
#Case 3: Test values > 1000000, not digit

print("{:^20}|{:^20}|{:^20}".format('Test data','Purpose','Expected results'))
print("{:^20}|".format('Tom, 3'))
print("{:^20}|".format('Dick, 36728'))
print("{:^20}|".format('Harry, 070asd329sa071saj'))

