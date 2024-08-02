import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user = "root",
    passwd="QaZWSXEDCRFVTGB2004%",
    database="employee_info"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

result = mycursor.fetchone()

for i in result:
    print(i)