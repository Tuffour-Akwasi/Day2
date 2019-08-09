import  mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'Pa$$001word',
    database = 'mydatabase',
    auth_plugin='mysql_native_password'
    )

mycursor = mydb.cursor()


'''sql = "SELECT * FROM customers WHERE address = %s%"

adr = ("box 54")

mycursor.execute(sql,adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)'''
#Sorting
''''sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
#ORDER BY DESC
'''sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)'''

#DELECT RECORD
'''sql = "DELETE FROM customers WHERE address = 'box 15'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) delete")'''

#PREVENT SQL INJECTION
'''sql = "DELETE FROM customers WHERE address = %s"
adr = ("Blue village",)
mycursor.execute(sql,adr)
mydb.commit()
print(mycursor.rowcount, "record(s) delect")'''

#DELECT A TABLE
'''sql = "DROP TABLE customers"
mycursor.execute(sql)'''

 #DROP IF IT EXISTS
'''sql = "DROP IF EXISTS customers"
mycursor.execute(sql)'''

#CREATE ANOTHER TABLE
'''mycursor.execute("CREATE TABLE ganster (name VARCHAR(255),address VARCHAR(255))")
'''
#INSERT NEW USER
'''sql = "INSERT INTO ganster (name, address) VALUES (%s, %s)"
val = ("Akiola","Highway 23")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted")
'''
#UPDATE USER
'''sql = "UPDATE ganster SET address = 'Loverock 12' WHERE address = 'Highway 23'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")
'''
#UPDATE USER %s
'''sql = "UPDATE ganster SET address = %s WHERE address = %s"
val = ("Highway 21","loverock 23")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")'''

#LIMIT
'''mycursor.execute("SELECT * FROM ganster LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)'''

#SELECT POS 3 N RETURN 5 REC
'''mycursor.execute("SELECT * FROM ganster LIMIT 3 OFFSET 1")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)'''

#CREATE A NEW TABLES
'''mycursor.execute("CREATE TABLE realhommies (product VARCHAR(255), brand VARCHAR(255))")
mycursor.execute("ALTER TABLE realhommies ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
sql = "INSERT INTO realhommies (product,brand) VALUES (%s ,%s)"
val = ("key Soup","mokola")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount,"record inserted")
'''
#JOINING TWO OR MORE TABLES
'''sql = "SELECT \
ganster.name As user, \
realhommies.product AS product \
FROM users\
INNER JOIN user ON user.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)'''
