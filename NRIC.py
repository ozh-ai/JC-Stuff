def validate_ID(idNo): #idNo is parameter, in string
    '''This function will validate an NRIC or FIN and returns either True or False'''

    if len(idNo)>9 or len(idNo)<9: #Check that string is of correct length
        return False
    else:
        if idNo[1:8].isdigit==False or idNo[0].isalpha==False or idNo[8].isalpha==False: #Check if string is in correct format
            return False
        else:
            total = int(idNo[1])*2 + int(idNo[2])*7 + int(idNo[3])*6 + int(idNo[4])*5 + int(idNo[5])*4 + int(idNo[6])*3 + int(idNo[7])*2 #Finds sum of products
            if idNo[0]=="T" or idNo[0]=="G":
                total = int(total) + 4   #Adds 4 to sum
            remainder = int(total) % 11  #Finds remainder
            checkdigit = 11 - remainder  #Finds check digit

            if idNo[0]=="S" or idNo[0]=="T":
                type = "NRIC"
            elif idNo[0]=="F" or idNo[0]=="G":
                type = "FIN"
            else:
                return False
            
            NRIClist = ["Nil","A","B","C","D","E","F","G","H","I","Z","J"]
            FINlist = ["Nil","K","L","M","N","P","Q","R","T","U","W","X"]

            if type == "NRIC":
                letter = NRIClist[checkdigit]
            else:
                letter = FINlist[checkdigit]
            if letter != idNo[8]:
                return False
            else:
                return True
            

def main():
    NRIC = input("What is your NRIC/FIN?")
    result = validate_ID(NRIC)
    print("NRIC/FIN is", result)
main()
