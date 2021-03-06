#######################################################################
## Name: MySQLConnection.py

## Purpose: Connect to MySQL server and return MySQLConnection object.

## Written/Edited by: Stanley Urbanek

## Date Created: 11/2/17

## Source:  https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
#######################################################################

import mysql.connector
from   mysql.connector import errorcode
import getpass

class MySQLConnection:

    def __init__(self):
        
        self.user = "user"
        self.pswd = "pswd"
        self.host = "host"
        self.db   = "db"
        
        self.cnx  = ""
        self.cnxMade = 0
    
    def openConnection(self):
    # Open connection to MySQL database
        
        # Prompt MySQL credentials
        self.user = raw_input("User: ")
        self.pswd = getpass.getpass("Password: ")
        self.host = raw_input("Host: ")
        self.db   = raw_input("Database: ")

        credentials = {
            'user': self.user,
            'password': self.pswd,
            'host': self.host,
            'database': self.db,
            'raise_on_warnings': True,
        }

        # If security is of concern, should sanitize input here
        
        # Initialize connection    
        try:
            self.cnx = mysql.connector.connect(**credentials)
            self.cnxMade = 1

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.cnx.close()

    def closeConnection(self):  
    # Close MySQL connection

        if self.cnxMade:
            self.cnx.close()
            self.cnxMade = 0

        return
