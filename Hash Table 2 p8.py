def hashfunction(keydata): #function (modular)
        total = 0
        for each in keydata: #for i in range(len(keydata)): total = total + ord(keydata[i])
            total = total + ord(each) #convert character to ASCII number, chr converts ASCII number to character
        return total % 9 # % gives the remainder after division

    
