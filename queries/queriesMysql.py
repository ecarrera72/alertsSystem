class queriesMysql(object):
    
    def getEquipo(self, db):
        try:
            query = "SELECT idcat_tipo_sistema FROM tbl_inventario_equipo"
            return db['instance'].runQuery(query, db)[0]
        except Exception as e:
            print(e)
            return False
    
    def getEstacionamiento(self, db):
        try:
            query = "SELECT * FROM estacionamientos WHERE Id_Estacionamientos = 1"
            return db['instance'].runQuery(query, db)[0]
        except Exception as e:
            print(e)
            return False