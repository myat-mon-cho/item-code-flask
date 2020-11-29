from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

@app.route('/productCode')
def hello_name():
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="bookstore1")
   mycursor=mysqldb.cursor()
   mycursor.execute('select * from product_code')
   values=mycursor.fetchall()
   return render_template('ProductCodeTableTest.html', values = values)

@app.route('/detail/<id>')
def getcookie(id):
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="bookstore1")
   mycursor=mysqldb.cursor()
   mycursor.execute('select * from product_code where p_id='+id)
   values=mycursor.fetchall()
   return render_template('ProductCodeDetailEdit.html', values = values)


@app.route('/updateSuccess',methods = ['POST', 'GET'])
def updateSuccess():
   if request.method == 'POST':
      p_id = request.form['p_id']
      p_name = request.form['p_name']
      v_description = request.form['v_description']
      identiier = request.form['p_identifier']
      variant = request.form['p_variant']
      f_type = request.form['f_type']
      g_code = request.form['g_code']
      sku = request.form['sku']
      p_code='P-'+identiier+variant+'-'+f_type+'-'+g_code+'-'+sku
      mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="bookstore1")
      mycursor=mysqldb.cursor()
      update_string="UPDATE product_code SET name='"+p_name+"', v_description='"+v_description+"', identiier='"+identiier+"', variant='"+variant+"', f_type='"+f_type+"', g_code='"+g_code+"', sku='"+sku+"', code='"+p_code+"' WHERE p_id="+p_id
      print(update_string)
      mycursor.execute(update_string)
      mysqldb.commit()
      if mycursor.rowcount > 0:
        mycursor.execute('select * from product_code where p_id='+p_id)
        values=mycursor.fetchall()
        return render_template('ProductCodeUpdateSuccess.html', values = values)
        #return ("Success") 
        #return redirect(url_for('ProductCodeUpdateSuccess.html',name = user))
      else:
         return ("Fail")
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


if __name__ == '__main__':
   app.run(debug = True)
