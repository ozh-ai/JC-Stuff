file = open('people.txt','r')
people = []
for line in file:
    people.append(line.strip().split(','))

import flask,sqlite3
from flask import render_template, request
app = flask.Flask(__name__)

@app.route('/')
def showdata():
    db = sqlite3.connect('Alvl 2020 Task 4.db')
    data = db.execute("SELECT FullName,ScreenName FROM People")
    data = data.fetchall()
    db.commit()
    db.close()
    length = len(data)

    identity = []
    for i in range(len(people)):
        if people[i][0] == data[i][0]:
            identity.append(people[i][2])
            
    return render_template('Alvl2020.html',data=data,identity=identity,length=length)

if __name__ == '__main__':
    app.run()
