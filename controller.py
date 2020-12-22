from database.sqlite import sqlite
from database.mysqldb import mysqldb
from config.config import config
from style.style import style
from time import sleep
import os, logging

class controller():
    objSqlite = None
    objMysql = None

    def __init__(self):
        self.objSqlite = sqlite()
        self.objMysql = mysqldb()
    
    def parking(self, varDB):
        obj = self.objMysql.connect(config().configDataBase(varDB))
        obj['instance'] = self.objMysql
        return obj

    def sqliteDataBase(self):
        query = "SELECT * FROM configDB"
        #return { a[0] : a[1] for a in self.objSqlite.runQuery(query) }
        return self.objSqlite.runQuery(query)

    def sqliteSystem(self):
        query = "SELECT * FROM configSYS"
        return { a[0] : a[1] for a in self.objSqlite.runQuery(query) }