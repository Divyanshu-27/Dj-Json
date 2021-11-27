from MySQLdb import cursors
from flask import Flask,jsonify
from flask_mysqldb import MySQL, MySQLdb 

app=Flask(__name__)

app.config ["MYSQL_HOST"] = "localhost"
app.config ["MYSQL_USER"] = "root"
app.config ["MYSQL_PASSWORD"]= "root"
app.config ["MYSQL_DB"]= "d1"
app.config ['JSON_SORT_KEYS']=False

mysql = MySQL(app)

@app.route('/user')
def user():
      try:


          cursors = mysql.connection.cursor()
          cursors.execute("select*from home")
          rows = cursors.fetchall()

      except Exception as e:
         print(e)

      finally:
         result=[]
         data={}
         for i in rows:
             data={
                'employee':i
                
                

              }
             
             result.append(data)
             data={}
             final_result={}
             final_result["success"] = 200
             final_result["message"] = 'API Is Working'
             final_result["output"] = result
             # json_comp=json.dumps(final_result)
              # return json_comp
      return jsonify(final_result)
       
    


















if __name__ == '__main__':
   app.run(debug=True)