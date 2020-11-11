from database.sqlite import sqlite
from database.mysqldb import mysqldb
from config.config import config
from coding.coding import coding
import os

class models(object):
    objSqlite = None
    objConfig = None
    objMysql = None

    def __init__(self):
        self.objSqlite = sqlite()
        self.objConfig = config(self.sqliteDataBase(), coding())
        self.objMysql = mysqldb()
    
    def parking(self, varDB):
        obj = self.objMysql.connect(self.objConfig.parking(varDB['CONEX_PARKINGDB'] , varDB))
        obj['instance'] = self.objMysql
        return obj

    def telemetria(self, varDB):
        obj = self.objMysql.connect(self.objConfig.telemetria(varDB['CONEX_TELEMETRIADB'] , varDB))
        obj['instance'] = self.objMysql
        return obj

    def sqliteData(self, database):
        query = "SELECT * FROM {}".format(database)
        return { a[0] : a[1] for a in self.objSqlite.runQuery(query) }

    # def sqliteSystem(self):
    #     query = "SELECT * FROM configSYS"
    #     return { a[0] : a[1] for a in self.objSqlite.runQuery(query) }