from style.style import style
from time import *
#import MySQLdb
import mysql.connector as my
import os

class mysqldb(style):

    def connect(self, data):
        try:
            #connect = my.connect(host=data['host'], port=int(data['port']), user=data['user'], passwd=data['passwd'], db=data['db'])
            connect = my.connect(**data)
            return { 'connect':connect, 'dataConnect':data }
        except Exception as e:
            self.errorMysql(e)

    def runQuery(self, query, db):
        try:
            if not db['connect'].is_connected(): db['connect'].reconnect(attempts=3, delay=2)

            cur = db['connect'].cursor(dictionary=True)
            cur.execute(query)

            if query.upper().startswith('SELECT'):
                data = cur.fetchall()
            else:
                db['connect'].commit()
                data = cur.lastrowid

            cur.close()
            return data
        except my.Error as e:
            self.errorMysql(e)
        except Exception as e:
            print(self.red(e))
            return False
    
    def reconnect(self, data):
        self.closeConnection(data)
        print(self.blue("Start reconnect"))
        return self.connect(data['dataConnect'])
    
    def closeConnection(self, data):
        print(self.purple("Close connection"))
        if data['cursor'] is not None:
            data['cursor'].close()
            data['cursor'] = None

        if data['connect'] is not None:
            data['connect'].close()
            data['connect'] = None

    def errorMysql(self, error):
        print('Error code:', error.errno)
        print('Sql state:', error.sqlstate)
        if error.errno == 2003:
            print('Message:', error.msg)
        os._exit(0)