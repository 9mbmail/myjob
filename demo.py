import mysql.connector
try:
    mydb = mysql.connector.connect(host="Mylocal",user="9mbmail",password="9A^37EVmdH@F49Euc")

    if mydb.is_connected():
        print("Connected")
except:
    print("Unable to connect")
