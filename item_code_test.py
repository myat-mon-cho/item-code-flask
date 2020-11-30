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

@app.route('/createProductCode')
def createProductCode():
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="bookstore1")
   mycursor=mysqldb.cursor()
   #mycursor.execute('select * from product_code where p_id='+id)
   #values=mycursor.fetchall()
   f_types = [{'name':'EC'}, {'name':'SC'}, {'name':'SL'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'SP'}, {'name' : 'GR'}, {'name' : 'WG'}, {'name' : 'TA'}, {'name' : 'OD'}, {'name' : 'FS'}, {'name' : 'DF'}, {'name' : 'CP'}, {'name' : 'FB'},  {'name' : 'OT'}, {'name' : 'SE'} ]
   g_codes = [{'name':'IN'}, {'name':'HE'}, {'name':'FU'}, {'name' : 'NF'}, {'name' : 'PG'}, {'name' : 'NE'}, {'name' : 'BA'}, {'name' : 'RO'}, {'name' : 'ST'}, {'name' : 'NC'}, {'name' : 'FB'}, {'name' : 'MO'}, {'name' : 'FT'}, {'name' : 'BP'}, {'name' : 'NS'},  {'name' : 'NT'}, {'name' : 'NA'}, {'name' : 'IF'}, {'name' : 'SU'}  ]
   #return ("Create Page")  
   return render_template('ProductCodeCreate.html', f_types=f_types, g_codes=g_codes)


@app.route('/detail/<id>')
def getcookie(id):
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="bookstore1")
   mycursor=mysqldb.cursor()
   mycursor.execute('select * from product_code where p_id='+id)
   values=mycursor.fetchall()
   f_types = [{'name':'EC'}, {'name':'SC'}, {'name':'SL'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'SP'}, {'name' : 'GR'}, {'name' : 'WG'}, {'name' : 'TA'}, {'name' : 'OD'}, {'name' : 'FS'}, {'name' : 'DF'}, {'name' : 'CP'}, {'name' : 'FB'},  {'name' : 'OT'}, {'name' : 'SE'} ]
   g_codes = [{'name':'IN'}, {'name':'HE'}, {'name':'FU'}, {'name' : 'NF'}, {'name' : 'PG'}, {'name' : 'NE'}, {'name' : 'BA'}, {'name' : 'RO'}, {'name' : 'ST'}, {'name' : 'NC'}, {'name' : 'FB'}, {'name' : 'MO'}, {'name' : 'FT'}, {'name' : 'BP'}, {'name' : 'NS'},  {'name' : 'NT'}, {'name' : 'NA'}, {'name' : 'IF'}, {'name' : 'SU'}  ]
      
   return render_template('ProductCodeDetailEdit.html', values = values, f_types=f_types, g_codes=g_codes)


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
      f_types = [{'name':'EC'}, {'name':'SC'}, {'name':'SL'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'SP'}, {'name' : 'GR'}, {'name' : 'WG'}, {'name' : 'TA'}, {'name' : 'OD'}, {'name' : 'FS'}, {'name' : 'DF'}, {'name' : 'CP'}, {'name' : 'FB'},  {'name' : 'OT'}, {'name' : 'SE'} ]
      g_codes = [{'name':'IN'}, {'name':'HE'}, {'name':'FU'}, {'name' : 'NF'}, {'name' : 'PG'}, {'name' : 'NE'}, {'name' : 'BA'}, {'name' : 'RO'}, {'name' : 'ST'}, {'name' : 'NC'}, {'name' : 'FB'}, {'name' : 'MO'}, {'name' : 'FT'}, {'name' : 'BP'}, {'name' : 'NS'},  {'name' : 'NT'}, {'name' : 'NA'}, {'name' : 'IF'}, {'name' : 'SU'}  ]
    
      mysqldb.commit()
      if mycursor.rowcount > 0:
        mycursor.execute('select * from product_code where p_id='+p_id)
        values=mycursor.fetchall()
        return render_template('ProductCodeUpdateSuccess.html', values = values, f_types=f_types, g_codes=g_codes)
        #return ("Success") 
        #return redirect(url_for('ProductCodeUpdateSuccess.html',name = user))
      else:
         return ("Fail")
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/createConfirm',methods = ['POST', 'GET'])
def createConfirm():
   if request.method == 'POST':
      
      p_name = request.form['p_name']
      v_description = request.form['v_description']
      identiier = request.form['p_identifier']
      variant = request.form['p_variant']
      f_type = request.form['f_type']
      g_code = request.form['g_code']
      sku = request.form['sku']
      p_code='P-'+identiier+variant+'-'+f_type+'-'+g_code+'-'+sku
      
      
      f_types = [{'name':'EC'}, {'name':'SC'}, {'name':'SL'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'SP'}, {'name' : 'GR'}, {'name' : 'WG'}, {'name' : 'TA'}, {'name' : 'OD'}, {'name' : 'FS'}, {'name' : 'DF'}, {'name' : 'CP'}, {'name' : 'FB'},  {'name' : 'OT'}, {'name' : 'SE'} ]
      g_codes = [{'name':'IN'}, {'name':'HE'}, {'name':'FU'}, {'name' : 'NF'}, {'name' : 'PG'}, {'name' : 'NE'}, {'name' : 'BA'}, {'name' : 'RO'}, {'name' : 'ST'}, {'name' : 'NC'}, {'name' : 'FB'}, {'name' : 'MO'}, {'name' : 'FT'}, {'name' : 'BP'}, {'name' : 'NS'},  {'name' : 'NT'}, {'name' : 'NA'}, {'name' : 'IF'}, {'name' : 'SU'}  ]
      return render_template('ProductCodeCreateConfirm.html',  f_types=f_types, g_codes=g_codes, p_name=p_name, v_description=v_description, identiier=identiier, variant=variant, f_type=f_type, g_code=g_code, sku=sku, p_code=p_code )
     


@app.route('/createSuccess',methods = ['POST', 'GET'])
def createSuccess():
   if request.method == 'POST':
      if request.form['action'] == "Confirm":
         
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
         sql = "INSERT INTO product_code ( name, v_description, identiier, variant, f_type, g_code, sku, code ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
         val = ( p_name, v_description, identiier, variant, f_type, g_code, sku, p_code)
        
         mycursor.execute(sql, val)
         
         mysqldb.commit()
         if mycursor.rowcount > 0:
            return render_template('ProductCodeCreateSuccess.html',   p_name=p_name, v_description=v_description, identiier=identiier, variant=variant, f_type=f_type, g_code=g_code, sku=sku, p_code=p_code )
           #return ("Success") 
           #return redirect(url_for('ProductCodeUpdateSuccess.html',name = user))
         else:
            
            return ("Fail")
      else:
         f_types = [{'name':'EC'}, {'name':'SC'}, {'name':'SL'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'SP'}, {'name' : 'GR'}, {'name' : 'WG'}, {'name' : 'TA'}, {'name' : 'OD'}, {'name' : 'FS'}, {'name' : 'DF'}, {'name' : 'CP'}, {'name' : 'FB'},  {'name' : 'OT'}, {'name' : 'SE'} ]
         g_codes = [{'name':'IN'}, {'name':'HE'}, {'name':'FU'}, {'name' : 'NF'}, {'name' : 'PG'}, {'name' : 'NE'}, {'name' : 'BA'}, {'name' : 'RO'}, {'name' : 'ST'}, {'name' : 'NC'}, {'name' : 'FB'}, {'name' : 'MO'}, {'name' : 'FT'}, {'name' : 'BP'}, {'name' : 'NS'},  {'name' : 'NT'}, {'name' : 'NA'}, {'name' : 'IF'}, {'name' : 'SU'}  ]
         return render_template('ProductCodeCreate.html', f_types=f_types, g_codes=g_codes)
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)
