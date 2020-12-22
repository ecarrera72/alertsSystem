from style.style import style
from time import sleep
import mysql.connector as my
import os, logging

class mysqldb(style):

    def connect(self, data):
        try:
            connect = my.connect(**data)
            return { 'connect': connect }
        except Exception as e:
            self.errorMysql(e, None)

    def runQuery(self, query, db):
        try:
            if not db['connect'].is_connected(): db['connect'].reconnect(attempts=3, delay=2)

            cur = db['connect'].cursor(dictionary=True)
            data = None
            cur.execute(query)

            if query.upper().startswith('SELECT'):
                data = cur.fetchall()
            else:
                db['connect'].commit()
                data = cur.lastrowid

            cur.close()
            return data
        except my.Error as e:
            self.errorMysql(e, db)
        except Exception as e:
            print(self.red(e))
            logging.error(e)
            return False
    
    def closeConnection(self, data):
        print(self.purple("Close connection"))
        if data['connect'] is not None: data['connect'].close()

    def errorMysql(self, error, db):
        print(self.red('Error code: {}'.format(error.errno)))
        if error.errno == 2003:
            print(self.red("Error: No se pudo conectar con el Servidor"))
        
        else:
            print(self.red('Message: {}'.format(error.msg)))

        if db is not None: 
            self.closeConnection(db)
            print("Is Connected {}".format(db['connect'].is_connected()))

        logging.error(error)

        sleep(3)
        os._exit(0)