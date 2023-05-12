import sqlite3 as sql
import mysql.connector as mysql

from flask import Flask, render_template, request, redirect, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder = '/home/aiona/flask_work')
Bootstrap(app)

conn = mysql.connect(
    host='localhost',
    user='project',
    password='aionalaw',
    database='hotel'
)

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS hotel(
         ReservationID INTEGER PRIMARY KEY,
         Name TEXT,
         Age INTEGER,
         Phone TEXT,
         Email TEXT,
         ResDate DATE)''')

print("Table Created Successfully")
conn.close()

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/register')
def register():
    return render_template('reservation.html')


@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        try:

            id = request.form['ReservationID']
            name = request.form['Name']
            age = request.form['Age']
            phone = request.form['Phone']
            email = request.form['Email']
            date = request.form['ResDate']

            with mysql.connect(
            host='localhost',
            user='project',
            password='aionalaw',
            database='hotel') as conn:

                c=conn.cursor()
                c.execute("INSERT INTO hotel (ReservationID,Name,Age,Phone,Email,Resdate) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(id,name,age,phone,email,date))
            
                conn.commit()
                msg = "Reservation successfully made"

        except:     
            conn.rollback()
            msg ="Error in insert operation"

        finally:
            return render_template("result.html", msg = msg)
            conn.close()


@app.route('/invoice')
def invoice():
    conn = mysql.connect(
        host='localhost',
        user='project',
        password='aionalaw',
        database ='hotel')
    
    conn.row_factory = sql.Row

    cur = conn.cursor()
    cur.execute("select * from hotel")
    rows = cur.fetchall()

    return render_template('invoice.html', rows = rows)

if __name__ == '__main__':
    app.run(debug = True)
    
