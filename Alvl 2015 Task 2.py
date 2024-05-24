#Task 2.1
def Converter(DenaryNumber):
    if DenaryNumber==0 or DenaryNumber==1:
        print(DenaryNumber,end='')
    else:
##        print(DenaryNumber%2,end='')
##        Converter(DenaryNumber//2)
        Converter(DenaryNumber//2)
        print(DenaryNumber%2,end='')

Converter(56)

#Task 2.2
'''The statements print(DenaryNumber%2,end='') and Converter(DenaryNumber//2) are in reverse order.
This causes the output to be in reverse.'''

#Task 2.3
print('\n')
print("{:^15}|{:^25}|{:^10}".format('DenaryNumber','Purpose','Expected output'))
print("{:^15}|{:^25}|{:^10}".format(23,'Normal data','10111'))
print("{:^15}|{:^25}|{:^10}".format(0,'Extreme data',0))
print("{:^15}|{:^25}|{:^10}".format(-1,'Abnormal data','Runtime Error'))


