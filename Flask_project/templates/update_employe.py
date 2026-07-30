import sqlite3

connect = sqlite3.connect("employe.db")
cursor = connect.cursor()

def update():

    name = input("Enter the name: ")
    print("1.Update name ")
    print("2.Update department ")
    print("3. Update Salary")
    choice = input("Enter your choice: ")

    while choice:

        if choice == "1":

            new_name = input("Enter the new name: ")


            cursor.execute(f"""
             UPDATE Products
             SET name = '{new_name}'
             WHERE name = '{name}';

             """) 
            break


        elif choice == "2":
            dep = input("Enter the new department: ")

            cursor.execute(f"""

             UPDATE Products 
             SET department = '{dep}'
             WHERE name = '{name}';


            """)
            break

        elif choice == "3":
            sal = input("Enter the new salary: ")

            cursor.execute(f"""

             UPDATE Products 
             SET salary = '{sal}'
             WHERE name = '{name}';



            """)
            break
    connect.commit()
    connect.close()


if __name__ == "__main__":
    update()



            