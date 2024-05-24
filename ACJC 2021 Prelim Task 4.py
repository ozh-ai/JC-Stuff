#Task 4.2
file = open('KIOSK.txt','r')
kiosk = []
for line in file:
    kiosk.append(line.strip().split(','))
file.close()

import sqlite3
db = sqlite3.connect('bento_company.db')
for i in range(len(kiosk)):
    db.execute('INSERT INTO Kiosk(KioskID,Location,Rating) VALUES(?,?,?)',(kiosk[i][0],kiosk[i][1],kiosk[i][2]))
    db.execute('INSERT INTO KioskBento(KioskID) VALUES(?)',(kiosk[i][0],))
    
file = open('BENTOBOX.txt','r')
bentobox = []
for line in file:
    bentobox.append(line.strip().split(','))
file.close()

for i in range(len(bentobox)):
    db.execute('INSERT INTO BentoBox(BentoName,ProductionCost,ContainEgg,ContainNut,ContainSeafood) VALUES(?,?,?,?,?)',
               (bentobox[i][0],bentobox[i][1],bentobox[i][2],bentobox[i][3],bentobox[i][4]))
    db.execute('INSERT INTO KioskBento(BentoName) VALUES(?)',(bentobox[i][0],))

pricelist = [0,2.6,2.9,2.4,3.1]
for i in range(len(kiosk)):
    for j in range(len(bentobox)):
        db.execute('INSERT INTO KioskBento(KioskID,BentoName,Sellprice) VALUES(?,?,?)',
                   (kiosk[i][0],bentobox[j][0],pricelist[int(kiosk[i][0])]+float(bentobox[j][1])))
    
db.commit()
db.close()

#Task 4.3
import flask,sqlite3
from flask import render_template,request
app = flask.Flask(__name__)

@app.route('/')
def form():
    return render_template('ACJC2021PrelimForm.html')

@app.route('/showdata/')
def showdata():
    if 'location' in request.args:
        location = request.args['location']
        allergies = request.args.getlist("allergy") #checkbox,radio button
        db = sqlite3.connect('bento_company.db')
        data = db.execute('SELECT * FROM Kiosk,BentoBox,KioskBento WHERE \
                          Kiosk.KioskID = KioskBento.KioskID AND \
                          BentoBox.BentoName = KioskBento.BentoName AND location=?',(location,)) #append all data which have correct location
        data = data.fetchall()

        result = []
        for i in range(len(data)):
            if ('egg' in allergies and data[i][5]==1) or ('nut' in allergies and data[i][6]==1) or ('seafood' in allergies and data[i][7]==1):
                pass
            else:
                result.append(data[i]) 
        length = len(result)
        db.commit()
        db.close()
        return render_template('ACJC2021PrelimResult.html',result=result,length=length)

if __name__ == '__main__':
    app.run()
        
        
    

