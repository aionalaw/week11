import sqlite3 as sql
import mysql.connector as mysql

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap


app = Flask(__name__, template_folder = '/home/aiona/flask_work' )
Bootstrap(app)

conn = mysql.connect(
   host='localhost',
   user='project',
   password='aionalaw',
   database = 'employee'
)

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employee (
          EmpID INTEGER PRIMARY KEY,
          EmpName TEXT,
          EmpGender TEXT,
          EmpPhone TEXT,
          EmpBdate DATE) ''')

print("Done")
conn.close()


@app.route('/')
def home():
   return render_template('home.html')



@app.route('/addrec',methods = ['GET','POST'])
def addrec():
   if request.method == 'POST':
      id = request.form['EmpID']
      name = request.form['EmpName']
      gender = request.form['EmpGender']
      phone = request.form['EmpPhone']
      bdate = request.form['EmpBdate']
         
      conn = mysql.connect(
         host='localhost',
         user='project',
         password='aionalaw',
         database='employee'
      )  
      c = conn.cursor()
      c.execute("INSERT INTO employee (EmpID, EmpName, EmpGender, EmpPhone, EmpBdate) VALUES ({0},{1},{2},{3},{4})" , (id,name,gender,phone,bdate))
   
      conn.commit()
      conn.close()

   return render_template('employee.html')

@app.route('/info')
def info():
   conn = mysql.connect(
      host='localhost',
      user='project',
      password='aionalaw',
      database='employee')
   
   cur = conn.cursor()
   cur.execute("select * from employee")
   rows = cur.fetchall(); 
   

   return render_template("info.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)

