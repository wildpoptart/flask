from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

con = sql.connect('database.db')
#con.execute('CREATE TABLE students (date DATE, jobID TEXT, jobName TEXT, userID TEXT, user TEXT, ontology TEXT, personnel TEXT, structure TEXT, infrastructure TEXT, vehicle TEXT, weapons TEXT, animals TEXT, totalFrames TEXT, completedFrames TEXT, lastFrame TEXT)')
con.close()

@app.route('/')
def home():
   return render_template('student.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         date =         request.form['date']
         jobID =        request.form['jobID']
         jobName =      request.form['jobName']
         user =         request.form['user']
         userID =       request.form['userID']
         ontology =     request.form['ontology']
         personnel =    request.form['personnel']
         structure =    request.form['structure']
         infrastructure = request.form['infrastructure']
         vehicle =      request.form['vehicle']
         weapons =      request.form['weapons']
         animals =      request.form['animals']
         totalFrames =  request.form['totalFrames']
         completedFrames = request.form['completedFrames']
         lastFrame =    request.form['lastFrame']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (date, jobID, jobName, userID, user, ontology, personnel, structure, infrastructure, vehicle, weapons, animals, totalFrames, completedFrames, lastFrame) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(date,jobID, jobName, userID, user, ontology, personnel, structure, infrastructure, vehicle, weapons, animals, totalFrames, completedFrames, lastFrame) )
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = con.Error.with_traceback()
         
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
    app.run(debug = True)