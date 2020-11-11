from style.style import style
#from time import *
import sqlite3
import os

class sqlite(style):
    _connect = None
    #_cursor = None
    
    def __init__(self):
        for root, dirs, files in os.walk(os.path.split(os.path.realpath(__file__))[0]):
            for name in files:
                if name.find("config.db") != -1:
                    self._connect = sqlite3.connect(os.path.join(root, name))
                    #self._cursor = self._connect.cursor()
    
    def runQuery(self, query):
        try:
            cursor = self._connect.cursor()
            cursor.execute(query)
            data = None

            if query.upper().startswith('SELECT'):
                data = cursor.fetchall()
                
            else:
                self._connect.commit()

            cursor.close()
            return data
        except Exception as e:
            print(self.red(e))
            return False