import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='',database='')
mycursor=con.cursor()
def check_connected():
    if con.is_connected():
        print("Succesful")
check_connected()
try:
    mycursor.execute("CREATE DATABASE sih")
    mycursor.execute("USE sih")
    print("Database created")
except:
    mycursor.execute("USE sih")
    print("Database Enhanced")
try:
    command="CREATE TABLE gpa(uname varchar(30),mail varchar(30),mobno int(12),keyv int(10))"
    mycursor.execute(command)
    print("Table has been created")
except:
    print("TABLE ENHANCED")

a=input('Enter Username:')
b=input("Enter the mailid:")
c=int(input("Enter the mobile number:"))
mycursor.execute("INSERT INTO student VALUES('{}','{}',{},{})".format(a,b,c,d))
print("Added data")
con.commit()

print("Now displaying the data")
mycursor.execute("SELECT*FROM gpa")
data=mycursor.fetchall()
for row in data:
    print(row)

