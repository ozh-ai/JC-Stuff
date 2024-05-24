def hextoden(hexa):
    global lettersden
    den = 0
    for i in range(len(hexa)):
        if hexa[i].isdigit():
            den = den + int(hexa[i])*(16**(len(hexa)-i-1))
        else:
            den = den + lettersden[letters.index(hexa[i])]*(16**(len(hexa)-i-1))
    return den

def dentohex(num):
    if num > 15:
        dentohex(num//16)
    num = num%16    
    if num in lettersden:
        num = letters[lettersden.index(num)]
    print(num,end='')

hexa = input("Enter hex number:")
letters = ['A','B','C','D','E','F']
lettersden = [10,11,12,13,14,15]
valid = True
for i in range(len(hexa)):
    if hexa[i].isdigit()==False and hexa[i].upper() not in letters:
        print("Not hex number!")
        valid = False
if valid == True:
    print(hextoden(hexa))

num = int(input("Enter num:"))
dentohex(num)


            
            
            
    
        
