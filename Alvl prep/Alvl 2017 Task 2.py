#Task 2.1
'''A: CalCheckDigit(Newnumber,Total)'''
'''B: return "X"'''
'''C: STRING(Number + CheckDigit)'''

#Task 2.2
def CalCheckDigit(number,total): #Calculate check digit
    if len(number)>1:
        digit = int(number[0])
        total = total+(digit*(len(number)+1))
        newnumber = number[1:]
        checkdigit = CalCheckDigit(newnumber,total)
    else:
        digit= int(number[0])
        total = total+(digit*(len(number)+1))
        CalcModulus = total%11
        CheckValue = 11 - CalcModulus
        if CheckValue==11:
            return str(0)
        else:
            if CheckValue==10:
                return 'X'
            else:
                return str(CheckValue)
    if len(number)==9:
        return str(number+checkdigit)
    else:
        return checkdigit
    
file = open('ISBNPRE.txt','r') #read data from file
isbn = []
for line in file:
    isbn.append(line.strip())
file.close() #close file
for i in range(len(isbn)):
    print(str(CalCheckDigit(isbn[i],0)))

    

