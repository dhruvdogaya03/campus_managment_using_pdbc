import mysql.connector


class Database:

    def connect(self):

        connection = mysql.connector.connect(host="localhost",port=3306,user="root",password="Dhruv@6263",database="pdbc_project")

        return connection

