#2.1
string = input("Enter string:")
stringlist = []
value = 0

for i in range(len(string)):
    if string[i].isupper() == True:
        value = ord(string[i]) + 13
        if value > 90:
            value = value - 26
        encoded = chr(value)
        stringlist.append(encoded)
    else:
        value = ord(string[i]) + 13
        if value > 122:
            value = value - 26
        encoded = chr(value)
        stringlist.append(encoded)
encodedstring = ''
for i in range(len(stringlist)):
    encodedstring = encodedstring + stringlist[i]
print(encodedstring)
    
#2.2
def encode(string):
    stringlist = []
    for i in range(len(string)):
        if string[i].isupper() == True:
            value = ord(string[i]) + 13
            if value > 90:
                value = value - 26
            encoded = chr(value)
            stringlist.append(encoded)
        else:
            value = ord(string[i]) + 13
            if value > 122:
                value = value - 26
            encoded = chr(value)
            stringlist.append(encoded)
    encodedstring = ''
    for i in range(len(stringlist)):
        encodedstring = encodedstring + stringlist[i]
    return encodedstring

string = input("Enter string:")
string = encode(string)
print(string)
encodedstring = encode(string)
print(encodedstring)

    
    
