from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

@app.route('/productCode')
def hello_name():
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="itemcode")
   mycursor=mysqldb.cursor()
   #mycursor.execute('select * from product_code')
   mycursor.execute('SELECT p.p_id, p.name, p.v_description,p.identiier, p.variant,f.formulation_notation, g.group_notation,p.sku, p.code,p.created FROM product_code p JOIN formulatype f ON p.f_type=f.f_id JOIN groupcode g ON p.g_code=g.g_id')
   values=mycursor.fetchall()
   return render_template('ProductCodeTableTest.html', values = values)

@app.route('/createProductCode')
def createProductCode():
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="itemcode")
   mycursor=mysqldb.cursor()
   mycursor.execute('select * from formulatype')
   f_types=mycursor.fetchall()
   mycursor.execute('select * from groupcode')
   g_codes=mycursor.fetchall()
   #f_types = [{'name':'EC'}, {'name':'SC'}, {'name':'SL'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'SP'}, {'name' : 'GR'}, {'name' : 'WG'}, {'name' : 'TA'}, {'name' : 'OD'}, {'name' : 'FS'}, {'name' : 'DF'}, {'name' : 'CP'}, {'name' : 'FB'},  {'name' : 'OT'}, {'name' : 'SE'} ]
   #g_codes = [{'name':'IN'}, {'name':'HE'}, {'name':'FU'}, {'name' : 'NF'}, {'name' : 'PG'}, {'name' : 'NE'}, {'name' : 'BA'}, {'name' : 'RO'}, {'name' : 'ST'}, {'name' : 'NC'}, {'name' : 'FB'}, {'name' : 'MO'}, {'name' : 'FT'}, {'name' : 'BP'}, {'name' : 'NS'},  {'name' : 'NT'}, {'name' : 'NA'}, {'name' : 'IF'}, {'name' : 'SU'}  ]
   #return ("Create Page")  
   return render_template('ProductCodeCreate.html', f_types=f_types, g_codes=g_codes)


@app.route('/detail/<id>')
def getcookie(id):
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="itemcode")
   mycursor=mysqldb.cursor()
   mycursor.execute('SELECT p.p_id,p.name, p.v_description,p.identiier, p.variant,f.formulation_notation, g.group_notation,p.sku, p.code,p.created, f.f_id, g.g_id FROM product_code p JOIN formulatype f ON p.f_type=f.f_id JOIN groupcode g ON p.g_code=g.g_id where p.p_id='+id)
   values=mycursor.fetchall()
   mycursor.execute('select * from formulatype')
   f_types=mycursor.fetchall()
   mycursor.execute('select * from groupcode')
   g_codes=mycursor.fetchall()
   #f_types = [{'name':'EC'}, {'name':'SC'}, {'name':'SL'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'SP'}, {'name' : 'GR'}, {'name' : 'WG'}, {'name' : 'TA'}, {'name' : 'OD'}, {'name' : 'FS'}, {'name' : 'DF'}, {'name' : 'CP'}, {'name' : 'FB'},  {'name' : 'OT'}, {'name' : 'SE'} ]
   #g_codes = [{'name':'IN'}, {'name':'HE'}, {'name':'FU'}, {'name' : 'NF'}, {'name' : 'PG'}, {'name' : 'NE'}, {'name' : 'BA'}, {'name' : 'RO'}, {'name' : 'ST'}, {'name' : 'NC'}, {'name' : 'FB'}, {'name' : 'MO'}, {'name' : 'FT'}, {'name' : 'BP'}, {'name' : 'NS'},  {'name' : 'NT'}, {'name' : 'NA'}, {'name' : 'IF'}, {'name' : 'SU'}  ]
      
   return render_template('ProductCodeDetailEdit.html', values = values, f_types=f_types, g_codes=g_codes)


@app.route('/updateSuccess',methods = ['POST', 'GET'])
def updateSuccess():
   if request.method == 'POST':
      mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="itemcode")
      mycursor=mysqldb.cursor()
      p_id = request.form['p_id']
      p_name = request.form['p_name']
      v_description = request.form['v_description']
      identiier = request.form['p_identifier']
      variant = request.form['p_variant']
      f_id = request.form['f_type']
      mycursor.execute('select formulation_notation from formulatype where f_id='+f_id)
      f_row=mycursor.fetchall()
      f_type=f_row[0][0]
      g_id = request.form['g_code']
      mycursor.execute('select group_notation from groupcode where g_id='+g_id)
      g_row=mycursor.fetchall()
      g_code=g_row[0][0]
      sku = request.form['sku']
      p_code='P-'+identiier+variant+'-'+f_type+'-'+g_code+'-'+sku
     
      update_string="UPDATE product_code SET name='"+p_name+"', v_description='"+v_description+"', identiier='"+identiier+"', variant='"+variant+"', f_type="+f_id+", g_code="+g_id+", sku='"+sku+"', code='"+p_code+"' WHERE p_id="+p_id
      print(update_string)
      mycursor.execute(update_string)
      mycursor.execute('select * from formulatype')
      f_types=mycursor.fetchall()
      mycursor.execute('select * from groupcode')
      g_codes=mycursor.fetchall()
      #f_types = [{'name':'EC'}, {'name':'SC'}, {'name':'SL'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'SP'}, {'name' : 'GR'}, {'name' : 'WG'}, {'name' : 'TA'}, {'name' : 'OD'}, {'name' : 'FS'}, {'name' : 'DF'}, {'name' : 'CP'}, {'name' : 'FB'},  {'name' : 'OT'}, {'name' : 'SE'} ]
      #g_codes = [{'name':'IN'}, {'name':'HE'}, {'name':'FU'}, {'name' : 'NF'}, {'name' : 'PG'}, {'name' : 'NE'}, {'name' : 'BA'}, {'name' : 'RO'}, {'name' : 'ST'}, {'name' : 'NC'}, {'name' : 'FB'}, {'name' : 'MO'}, {'name' : 'FT'}, {'name' : 'BP'}, {'name' : 'NS'},  {'name' : 'NT'}, {'name' : 'NA'}, {'name' : 'IF'}, {'name' : 'SU'}  ]
    
      mysqldb.commit()
      if mycursor.rowcount > 0:
        mycursor.execute('SELECT p.p_id,p.name, p.v_description,p.identiier, p.variant,f.formulation_notation, g.group_notation,p.sku, p.code,p.created, f.f_id, g.g_id FROM product_code p JOIN formulatype f ON p.f_type=f.f_id JOIN groupcode g ON p.g_code=g.g_id where p.p_id='+p_id)
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
      mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="itemcode")
      mycursor=mysqldb.cursor()
      p_name = request.form['p_name']
      v_description = request.form['v_description']
      mycursor.execute('SELECT MAX(identiier) FROM product_code')
      i_row=mycursor.fetchall()
      max_identiier=i_row[0][0]
      identiier = max_identiier+1
      variant = request.form['p_variant']
      #f_type = request.form['f_type']
      #g_code = request.form['g_code']
      f_id = request.form['f_type']
      mycursor.execute('select formulation_notation from formulatype where f_id='+f_id)
      f_row=mycursor.fetchall()
      f_type=f_row[0][0]
      g_id = request.form['g_code']
      mycursor.execute('select group_notation from groupcode where g_id='+g_id)
      g_row=mycursor.fetchall()
      g_code=g_row[0][0]
      sku = request.form['sku']
      p_code='P-'+str(identiier)+variant+'-'+f_type+'-'+g_code+'-'+sku
      
      mycursor.execute('select * from formulatype')
      f_types=mycursor.fetchall()
      mycursor.execute('select * from groupcode')
      g_codes=mycursor.fetchall()
      #f_types = [{'name':'EC'}, {'name':'SC'}, {'name':'SL'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'WP'}, {'name' : 'SP'}, {'name' : 'GR'}, {'name' : 'WG'}, {'name' : 'TA'}, {'name' : 'OD'}, {'name' : 'FS'}, {'name' : 'DF'}, {'name' : 'CP'}, {'name' : 'FB'},  {'name' : 'OT'}, {'name' : 'SE'} ]
      #g_codes = [{'name':'IN'}, {'name':'HE'}, {'name':'FU'}, {'name' : 'NF'}, {'name' : 'PG'}, {'name' : 'NE'}, {'name' : 'BA'}, {'name' : 'RO'}, {'name' : 'ST'}, {'name' : 'NC'}, {'name' : 'FB'}, {'name' : 'MO'}, {'name' : 'FT'}, {'name' : 'BP'}, {'name' : 'NS'},  {'name' : 'NT'}, {'name' : 'NA'}, {'name' : 'IF'}, {'name' : 'SU'}  ]
      return render_template('ProductCodeCreateConfirm.html',  f_types=f_types, g_codes=g_codes, p_name=p_name, v_description=v_description, identiier=identiier, variant=variant, f_type=f_type, g_code=g_code, sku=sku, p_code=p_code )
     


@app.route('/createSuccess',methods = ['POST', 'GET'])
def createSuccess():
   if request.method == 'POST':
      if request.form['action'] == "Confirm":
         mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="itemcode")
         mycursor=mysqldb.cursor()
         p_name = request.form['p_name']
         v_description = request.form['v_description']
         identiier = request.form['p_identifier']
         variant = request.form['p_variant']
         f_notation = request.form['f_type']
         mycursor.execute("select f_id from formulatype where formulation_notation='"+f_notation+"'")
         f_row=mycursor.fetchall()
         f_type=f_row[0][0]
         g_notation = request.form['g_code']
         mycursor.execute("select g_id from groupcode where group_notation='"+g_notation+"'")
         g_row=mycursor.fetchall()
         g_code=g_row[0][0]
         sku = request.form['sku']
         p_code='P-'+identiier+variant+'-'+f_notation+'-'+g_notation+'-'+sku
        
         
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

@app.route('/duplicateSuccess',methods = ['POST', 'GET'])
def duplicateSuccess():
   if request.method == 'POST':
      if request.form['action'] == "Duplicate":
         mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="itemcode")
         mycursor=mysqldb.cursor()
         p_name = request.form['p_name']
         v_description = request.form['v_description']
         identiier = request.form['p_identifier']
         variant = request.form['p_variant']
         f_notation = request.form['f_type']
         mycursor.execute("select f_id from formulatype where formulation_notation='"+f_notation+"'")
         f_row=mycursor.fetchall()
         f_type=f_row[0][0]
         g_notation = request.form['g_code']
         mycursor.execute("select g_id from groupcode where group_notation='"+g_notation+"'")
         g_row=mycursor.fetchall()
         g_code=g_row[0][0]
         sku = request.form['sku']
         p_code='P-'+identiier+variant+'-'+f_notation+'-'+g_notation+'-'+sku
        
         
         sql = "INSERT INTO product_code ( name, v_description, identiier, variant, f_type, g_code, sku, code ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
         
         val = ( p_name, v_description, identiier, variant, f_type, g_code, sku, p_code)
        
         mycursor.execute(sql, val)
         
         mysqldb.commit()
         if mycursor.rowcount > 0:
            p_id=mycursor.lastrowid
            mycursor.execute('SELECT p.p_id,p.name, p.v_description,p.identiier, p.variant,f.formulation_notation, g.group_notation,p.sku, p.code,p.created, f.f_id, g.g_id FROM product_code p JOIN formulatype f ON p.f_type=f.f_id JOIN groupcode g ON p.g_code=g.g_id where p.p_id='+str(p_id))
            values=mycursor.fetchall()
            mycursor.execute('select * from formulatype')
            f_types=mycursor.fetchall()
            mycursor.execute('select * from groupcode')
            g_codes=mycursor.fetchall()
            return render_template('ProductCodeDuplicateSuccess.html', values=values,f_types=f_types, g_codes=g_codes)
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
