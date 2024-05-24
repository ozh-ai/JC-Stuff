file = open('JARGON.txt','r')
contents = []
for line in file:
    contents.append(line.strip())
file.close()

while True:
    print("+"*20)
    print("1. Exact Match\n2. Start of term\n3. Within term")
    print("+"*16)
    choice = input("Choice?")
    if choice == '1':
        term = input("Term?")
        count = 0
        for i in range(len(contents)):
            if contents[i] == term:
                count = count+1
        print("There were",count,"matching term(s)")
    elif choice == '2':
        term = input("Term?")
        count = 0
        for i in range(len(contents)):
            if contents[i].startswith(term) == True:
                print(contents[i])
                count = count+1
        print("There were",count,"matching term(s)")
    elif choice == '3':
        term = input("Term?")
        count = 0
        for i in range(len(contents)):
            if term in contents[i]:
                print(contents[i])
                count = count+1
        print("There were",count,"matching term(s)")



