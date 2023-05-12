from flask import Flask
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost", user="project", password="aionalaw"
)

cur = conn.cursor()
print(conn)

cmd = "CREATE DATABASE hotel"
cur.execute(cmd)
conn.close()

