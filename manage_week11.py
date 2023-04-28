from flask import Flask, url_for, redirect, render_template, request


import sqlite3 as sql
app = Flask(__name__)

conn = sql.connect('employee.db')
c = conn.cursor()
c.execute('''CREATE TABLE employee (
          EmpName TEXT,
          EmpGender TEXT,
          EmpPhone TEXT,
          EmpBdate DATE) ''')

print("Done")
conn.close()


@app.route('/')
def home():
   return render_template('home.html')



@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      name = request.form['EmpName']
      gender = request.form['EmpGender']
      phone = request.form['EmpPhone']
      bdate = request.form['EmpBdate']
         
      conn = sql.connect('employee.db')  
      c = conn.cursor()
      c.execute("INSERT INTO employee (EmpName,EmpGender,EmpPhone,EmpBdate) VALUES (?,?,?,?)" , (name,gender,phone,bdate))
   
      conn.commit()
      conn.close()

@app.route('/info')
def info():
   with sql.connect('employee.db') as con:
      cur = con.cursor()
      cur.execute("select * from employee")
      rows = cur.fetchall(); 
   

   
   return render_template("info.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)

