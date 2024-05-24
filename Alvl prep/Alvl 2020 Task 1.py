#Task 1.1

def task1_1(string_value):
    h = 0
    for i in range(len(string_value)-1):
        val = 33*ord(string_value[i])
        h = (h + val) % 1024
    return h
        
print(task1_1("Hello"))
print(task1_1("Hallo"))
print(task1_1("Hullo"))

#Task 1.2
def task1_2(seed,string_value):
    result = seed + string_value
    print(task1_1(result))

task1_2("seed-one","Hello")
task1_2("seed-two","Hello")
task1_2("seed-three","Hello")

    

    
