#Task 3.1
def second_dose_date(date):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    date = int(date)
    date = date + 21
    date = str(date)
    if int(date[-2:]) > days[int(date[4:6])-1]:
        month = str(int(date[4:6])+1)
        day = int(date[-2:]) - days[int(date[4:6])-1]
        if len(month)==1:
            month = '0'+month
        if len(str(day))==1:
            day = '0'+str(day)
        date = '2021'+month+str(day)
        if int(month)>12:
            date = '2022'+'01'+day
    return date

print(second_dose_date('20210105'))
print(second_dose_date('20210212'))
print(second_dose_date('20210919'))

#Task 3.2
file = open('VACCINATION.txt','r')
member = []
for line in file:
    member.append(line.strip().split(','))
file.close()

import pymongo
client = pymongo.MongoClient('127.0.0.1',27017)
db = client.get_database('community_centre')
try:
    db.drop_database('management_committee')
except:
    pass
coll = db.get_collection('management_committee')

##alt:
##if coll.find().count != 0:
##    coll.delete_many({}) #clear the collection

addlist = []
for i in range(len(member)):
    if len(member[i]) == 5:
        addlist.append({'id':member[i][0],'name':member[i][1],'date_first_dose':member[i][2],'date_second_dose':member[i][3],'remarks':member[i][4]})
    elif len(member[i]) == 4:
        if type(member[i][-1]) == str:
            addlist.append({'id':member[i][0],'name':member[i][1],'date_first_dose':member[i][2],'remarks':member[i][-1]})
        else:
            addlist.append({'id':member[i][0],'name':member[i][1],'date_first_dose':member[i][2],'date_second_dose':member[i][3]})
    elif len(member[i]) == 3:
        if type(member[i][-1]) == str:
            addlist.append({'id':member[i][0],'name':member[i][1],'remarks':member[i][-1]})
        else:
            addlist.append({'id':member[i][0],'name':member[i][1],'date_first_dose':member[i][2]})
    else:
        addlist.append({'id':member[i][0],'name':member[i][1]})
coll.insert_many(addlist)

#Task 3.3
userid = input("Enter userid:")
while userid.isdigit() == False:
    userid = input("Enter userid:")
result = coll.find_one({'id':int(user)})
if result.count({'id':userid})>0:
    if result.count({'id':userid,'date_first_dose':{'$exists':True},'date_second_dose':{'$exists':True}}):
        result = coll.find({'id':userid,'date_first_dose':{'$exists':True},'date_second_dose':{'$exists':True}})
        file = open('VACCINATION.txt','w')
        file.write('VACCINATION CERTIFICATE\n')
        for document in result:
            file.write('\nName:',document.get('name'),'\nVaccine type: CoviDie\nDate of first dose:',document.get('date_first_dose'),
                       '\nDate of second dose:',document.get('date_second_dose'))
        
        for document in result:
            search = {'id':userid,'date_first_dose':{'$exists':True},'date_second_dose':{'$exists':True}}
            update = {'cert':{'$set':'yes'}}
            coll.update_one(search,update)

    elif result.count({'id':userid,'date_first_dose':{'$exists':True},'date_second_dose':{'$exists':False}}):
        result = coll.find({'id':userid,'date_first_dose':{'$exists':True},'date_second_dose':{'$exists':True}})
        for document in result:
            date = second_dose_date(document.get('date_first_dose'))
            print('2nd date is',date)

    else:
        print('Take the first dose as soon as possible.')
            
        
        


