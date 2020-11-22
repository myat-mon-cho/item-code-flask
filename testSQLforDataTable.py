from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

@app.route('/')
def hello_name():
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="bookstore")
   mycursor=mysqldb.cursor()
   mycursor.execute('select * from book')
   values=mycursor.fetchall()
   return render_template('ProductCodeTableStatic.html', values = values)


if __name__ == '__main__':
   app.run(debug = True)