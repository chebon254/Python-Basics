import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Shop"
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)

# If the table already exists, use the ALTER TABLE keyword:
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#      print(x)


# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "records inserted.")
# print(mycursor.rowcount, "records inserted, ID: ", mycursor.lastrowid)





# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)






# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)









# PREVENT SQL INJECTION - Escape query values by using the placholder %s method:


# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)










# DESC


# sql = "SELECT * FROM customers ORDER BY name DESC"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


















# DELETE

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")






# LIMIT

mycursor.execute("INSERT INTO `Customers`(CustomerName, CustomerContact, Address, City, Code, Country) VALUES ('Cardinal','Tom B. Erichsen','Skagen','Stavanger','4006','Norway')")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)
