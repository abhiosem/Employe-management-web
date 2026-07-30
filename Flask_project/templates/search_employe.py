import sqlite3

connect = sqlite3.connect("employe.db")
cursor = connect.cursor()

def search():
    name = input("Enter the employe name you want to search about: ")

    cursor.execute("""SELECT name,department,salary
                      FROM Products
                      WHERE name = ?""",
                      (name,)
    )
    row = cursor.fetchone()

    if row:

        name,department,salary = row 

        print(f"Name: {name}")
        print(f"Department: {department}")
        print(f"Salary: {salary}")


    connect.commit()
    connect.close()

if __name__ == "__main__":
    search()
        