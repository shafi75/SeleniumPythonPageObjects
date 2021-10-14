import mysql.connector

def createDbConnection():
    global  mydb
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="faizi_FORu65",
        database="pydbprac"
    )


def getMySQlQuery(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchone()
    return myresult[0]
