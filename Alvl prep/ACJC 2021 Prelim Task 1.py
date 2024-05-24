#Task 1.1
def validate(num):
    num = num.replace(' ','')
    if len(num)==12 and num.isdigit()==True:
        value = 0
        for i in range(12):
            if i==0 or i==2 or i==4 or i==6 or i==8 or i==10:
                value = value + 3*(int(num[i]))
            else:
                value = value + int(num[i])
        value = value%10
        if value==0:
            return 'Valid'
    return 'Invalid'

print(validate('036000 291452'))

#Task 1.2
def convert(ID):
    table = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    ID = ID.replace(' ','')
    start = '000000000 101 '
    mid = '01010 '
    end = '101 000000000'
    firstsix = ''
    for i in range(6):
        firstsix = firstsix + table[int(ID[i])]
        firstsix = firstsix + ' '
    lastsix = ''
    for i in range(6,12):
        lastsix = lastsix + table[int(ID[i])]
        lastsix = lastsix + ' '
    lastsix = lastsix.replace('0','a')
    lastsix = lastsix.replace('1','b')
    lastsix = lastsix.replace('a','1')
    lastsix = lastsix.replace('b','0')
    barcode = start + firstsix + mid + lastsix + end
    return barcode

print(convert('036000 291452'))

#Task 1.3
def converttoID(barcode):
    table = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    barcode = barcode.replace(' ','')
    if len(barcode)!=113 or barcode.isdigit()==False:
        return 'Invalid barcode'
    if (barcode[12:19].count('1'))%2==0: #if upside down
        newbarcode = ''
        for i in range(1,len(barcode)+1):
            j = 0-i
            newbarcode = newbarcode+barcode[j]
        barcode = newbarcode
    barcode = barcode.replace('000000000101','')
    barcode = barcode.replace('101000000000','')
    ID = '' 
    for i in range(6):
        if barcode[7*i:(7*i)+7] not in table:
            return 'Invalid barcode'
        ID = ID + str(table.index(barcode[7*i:(7*i)+7]))
    barcode = barcode[47:]
    for i in range(6):
        sixdigit = barcode[7*i:(7*i)+7]
        sixdigit = sixdigit.replace('0','a')
        sixdigit = sixdigit.replace('1','b')
        sixdigit = sixdigit.replace('a','1')
        sixdigit = sixdigit.replace('b','0')
        if sixdigit not in table:
            return 'Invalid barcode'
        ID = ID + str(table.index(sixdigit))
    return ID

print(converttoID('000000000 101 0001101 0111101 0101111 0001101 0001101 0001101 01010 1101100 1110100 1100110 1011100 1001110 1101100 101 000000000'))

        
        
        
        










        
    
