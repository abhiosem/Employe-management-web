from flask import Flask,render_template,request
import sqlite3


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")


@app.route("/submit",methods = ["POST"])
def submit():

            name = request.form["name"]
            department = request.form["department"]
            salary = request.form["salary"]


            connect = sqlite3.connect("employe.db")
            cursor = connect.cursor()
            
            cursor.execute("""
             CREATE TABLE IF NOT EXISTS employes(
              id INTEGER PRIMARY KEY,
              name TEXT,
              department TEXT,
              salary REAL
                 
                 )
                """)
            cursor.execute(
                   "INSERT INTO employes(name,department,salary) VALUES(?,?,?)",
            (name,department,salary)
            )
            connect.commit()
            connect.close()

            return "<h1> Added succesfully! </h1>"
    
    
    
    
  
app.run(debug=True)