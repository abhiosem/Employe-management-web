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

@app.route("/employes")
def open():
        connect = sqlite3.connect("employe.db")
        cursor = connect.cursor()

        cursor.execute("SELECT * FROM employes")

        employee = cursor.fetchall()
                

        connect.commit()
        connect.close()

        return render_template("employe.html",employee=employee)
                
@app.route("/add")
def add():
        return render_template("form.html")



@app.route("/search")
def search_page():
        return render_template("search.html")


        
@app.route("/search", methods=["POST"])
def search():
        check = request.form["name"]

        connect = sqlite3.connect("employe.db")
        cursor = connect.cursor()

        cursor.execute(
            "SELECT * FROM employes WHERE name = ?",
            (check,)
        )

        ho = cursor.fetchall()
        print(ho)
        connect.close()

        return render_template("search.html", ho=ho)


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):

    connect = sqlite3.connect("employe.db")
    cursor = connect.cursor()

    if request.method == "POST":

        name = request.form["name"]
        department = request.form["department"]
        salary = request.form["salary"]

        cursor.execute("""
            UPDATE employes
            SET
                name = ?,
                department = ?,
                salary = ?
            WHERE id = ?
        """, (name, department, salary, id))

        connect.commit()

    cursor.execute(
        "SELECT * FROM employes WHERE id = ?",
        (id,)
    )

    employee = cursor.fetchone()

    connect.close()

    return render_template("update.html", employee=employee)






        
           
     
                       
  
app.run(debug=True)
       
    
