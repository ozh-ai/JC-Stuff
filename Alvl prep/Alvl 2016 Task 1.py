#1.1
##import random
##numberlist = []
##for i in range(1000):
##    number = random.randint(1,20)
##    numberlist.append(number)
##
##print("{:^10}|{:^10}".format("Integer","Frequency"))
##for i in range(1,21):
##    freq = numberlist.count(i)
##    print("{:^10}|{:^10}".format(i,freq))

#1.2
import random
numberlist = []
for i in range(1000):
    number = random.randint(1,20)
    numberlist.append(number)

exp = 1000/20
print("Expected frequency:", exp)

print("{:^10}|{:^10}|{:^10}".format("Integer","Frequency","Difference"))
for i in range(1,21):
    freq = numberlist.count(i)
    diff = abs(exp-freq)
    print("{:^10}|{:^10}|{:^10}".format(i,freq,diff))



    
