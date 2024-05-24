#Task 2.2
class ServiceRecord:
    def __init__(self,sender,accessdate,status,apptype): #constructor
        self.__sender = sender
        self.__accessdate = accessdate
        self.__status = status
        self.__apptype = apptype

    def getapptype(self):
        return self.__apptype
    def getsender(self):
        return self.__sender
    def getaccessdate(self):
        return self.__accessdate
    def getstatus(self):
        return self.__status

    def isSuccess(self):
        if self.__status == 200:
            return True
        else:
            return False

#Task 2.3
class AppServiceRecord(ServiceRecord):
    def __init__(self,sender,accessdate,status,apptype): #constructor
        super().__init__(sender,accessdate,status,apptype)

    def getapptype(self):
        if self.__apptype=='WA':
            return 'WHATSAPP'
        elif self.__apptype=='FB':
            return 'FACEBOOK MESSENGER'

    def getSuccess(self):
        boolean = super().isSuccess() #returns True or False
        if boolean==True:
            return 'SUCCESS'
        elif boolean==False:
            return 'FAILED'

class SmsServiceRecord(ServiceRecord):
    def __init__(self,sender,accessdate,status,apptype):
        super().__init__(sender,accessdate,status,apptype)
        
    def getapptype(self):
        return 'SHORT MESSAGE SERVICE'
    def getSuccess(self):
        boolean = super().isSuccess() #returns True or False
        if boolean==True:
            return 'SUCCESS'
        elif boolean==False:
            return 'FAILED'

file = open('LOG.txt','r')
data = []
for line in file:
    data.append(line.strip().split(' '))
data.pop(-1)
file.close()
print(data)

record = []
for i in range(len(data)):
    if len(data[i])==3:
        record.append(ServiceRecord(data[i][0],data[i][1],data[i][2],''))
    else:
        record.append(ServiceRecord(data[i][0],data[i][1],data[i][2],data[i][3]))

#Task 2.4
import flask
from flask import render_template,request
app = flask.Flask(__name__)

@app.route('/')
def display():
    senderlist = []
    datelist = []
    typelist = []
    statuslist = []
    for i in range(len(record)):
        senderlist.append(record[i].getsender())
        datelist.append(record[i].getaccessdate())
        if record[i].getapptype() == 'WA':
            typelist.append('WHATSAPP')
        elif record[i].getapptype() == 'FB':
            typelist.append('FACEBOOK MESSENGER')
        else:
            typelist.append('SHORT MESSAGE SERVICE')
            
        if int(record[i].getstatus()) == 200:
            statuslist.append('SUCCESS')
        else:
            statuslist.append('FAILED')
            
    print(typelist)
    length = len(senderlist)
    return render_template('display.html',senderlist=senderlist,datelist=datelist,typelist=typelist,statuslist=statuslist,length=length)
    
if __name__ == '__main__':
    app.run()


    
    

        
