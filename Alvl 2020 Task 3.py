#Task 3.1
def task3_1(quantity_of_data):
    approved = ['KB','MB','GB','TB']
    if quantity_of_data[0:-2].isdigit == False:
        print("Invalid data")
    else:
        if quantity_of_data[-2:] == 'KB': #if quantity_of_data.endswith('KB'):  #same for startswith
            result = int(quantity_of_data[0:-2])*(10**3)
        elif quantity_of_data[-2:] == 'MB':
            result = int(quantity_of_data[0:-2])*(10**6)
        elif quantity_of_data[-2:] == 'GB':
            result = int(quantity_of_data[0:-2])*(10**9)
        elif quantity_of_data[-2:] == 'TB':
            result = int(quantity_of_data[0:-2])*(10**12)
        else:
            print("Invalid data")
        print(result, "bytes")

#Task 3.2
def task3_2(quantity_of_data):
    approved = ['KB','KiB','MB','MiB','GB','GiB','TB','TiB']
    if (quantity_of_data[-2] + quantity_of_data[-1]) not in approved and (quantity_of_data[-3] + quantity_of_data[-2] + quantity_of_data[-1]) not in approved:
            return "Invalid data"
    elif quantity_of_data[0:-2].isdigit == False:
        return "Invalid data"
    else:
        if (quantity_of_data[-2] + quantity_of_data[-1]) == 'KB':
            result = int(quantity_of_data[0:-2])*(10**3)
        elif (quantity_of_data[-2] + quantity_of_data[-1]) == 'MB':
            result = int(quantity_of_data[0:-2])*(10**6)
        elif (quantity_of_data[-2] + quantity_of_data[-1]) == 'GB':
            result = int(quantity_of_data[0:-2])*(10**9)
        elif (quantity_of_data[-2] + quantity_of_data[-1]) == 'TB':
            result = int(quantity_of_data[0:-2])*(10**12)
        elif (quantity_of_data[-3] + quantity_of_data[-2] + quantity_of_data[-1]) == 'KiB':
            result = int(quantity_of_data[0:-3])*(2**10)
        elif (quantity_of_data[-3] + quantity_of_data[-2] + quantity_of_data[-1]) == 'MiB':
            result = int(quantity_of_data[0:-3])*(2**20)
        elif (quantity_of_data[-3] + quantity_of_data[-2] + quantity_of_data[-1]) == 'GiB':
            result = int(quantity_of_data[0:-3])*(2**30)
        elif (quantity_of_data[-3] + quantity_of_data[-2] + quantity_of_data[-1]) == 'TiB':
            result = int(quantity_of_data[0:-3])*(2**40)
        return result

##print(task3_2('4TiB'))

#Task 3.3
def task3_3(quantity_of_data, target_unit):
    approved = ['KB','KiB','MB','MiB','GB','GiB','TB','TiB']
    if target_unit not in approved:
        return "Invalid data"
    byte = task3_2(quantity_of_data)
    if byte == 'Invalid data':
        return 'Invalid data' 
    elif target_unit == 'KB':
        result = int(byte)/(10**3)
    elif target_unit == 'MB':
        result = int(byte)/(10**6)
    elif target_unit == 'GB':
        result = int(byte)/(10**9)
    elif target_unit == 'TB':
        result = int(byte)/(10**12)
    elif target_unit == 'KiB':
        result = int(byte)/(2**10)
    elif target_unit == 'MiB':
        result = int(byte)/(2**20)
    elif target_unit == 'GiB':
        result = int(byte)/(2**30)
    elif target_unit == 'TiB':
        result = int(byte)/(2**40)
    return result

print(task3_3('512MiB','GiB')) #Have at least 1 valid, 1 invalid
print(task3_3('100000TaB','TiB'))
print(task3_3('12345KiB','KB'))
    
            
        
        
