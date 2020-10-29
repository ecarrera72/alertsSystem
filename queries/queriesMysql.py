class queriesMysql(object):
    
    def getEquipo(self, db):
        try:
            query = "SELECT idcat_tipo_equipo FROM cat_tipo_equipo WHERE cat_tipo_equipo_default = 1"
            return db['instance'].runQuery(query, db)[0]
        except Exception as e:
            print(e)
            return False
    
    def getConfigCircuit(self, db, id):
        try:
            query = "SELECT * FROM tbl_configuracion_equipo WHERE idcat_tipo_equipo = {}".format(id)
            return db['instance'].runQuery(query, db)
        except Exception as e:
            print(e)
            return False
    
    def setOverwritePortSerial(self, db, correctPort, errorPort, id):
        try:
            querys = []
            querys.append("UPDATE tbl_configuracion_equipo SET tbl_configuracion_equipo_puerto = '{}' WHERE tbl_configuracion_equipo_puerto = '{}'".format(errorPort, correctPort))
            querys.append("UPDATE tbl_configuracion_equipo SET tbl_configuracion_equipo_puerto = '{}' WHERE idtbl_configuracion_equipo = '{}'".format(correctPort, id))
            [db['instance'].runQuery(x, db) for x in querys]
        except Exception as e:
            print(e)
            return False
    
    def getConfigCircuitDet(self, db, id):
        try:
            query = "SELECT * FROM tbl_configuracion_equipo_detalle WHERE idtbl_configuracion_equipo = {}".format(id)
            return db['instance'].runQuery(query, db)
        except Exception as e:
            print(e)
            return False
    
    def getDataUser(self, db, code):
        try:
            query = """SELECT tarj_id, tarj_activo, tarj_tipta_id, tarj_estatus_antipb, tarj_estatus_pago, pnds_id, pnds_activo 
                        FROM tbl_tarjetas JOIN tbl_pensionados ON pnds_tarj_id = tarj_id 
                        WHERE tarj_codigo LIKE '{}%'""".format(code)
            return db['instance'].runQuery(query, db)
        except Exception as e:
            print(e)
            return False
    
    def insertDataUser(self, db, user, circuit, code):
        try:
            antipass = 1
            querys = []
            if user['error'] == 1:
                querys.append("""INSERT INTO tbl_movimientos_pensionados (mope_lectura, mope_fecha, mope_hora, 
                                mope_evento, mope_cea_id_int, mope_id_usuarios) VALUES ('{}', {}, {}, '{}', {}, {})
                                """.format(code, 'NOW()', 'NOW()', circuit['tbl_configuracion_equipo_posicion'][:1], user['error'], 
                                            circuit['idtbl_configuracion_equipo']))    
            else:
                querys.append("""INSERT INTO tbl_movimientos_pensionados(mope_tarj_id, mope_pnds_id, mope_fecha, 
                                mope_hora, mope_evento, mope_cea_id_int, mope_id_usuarios) 
                                VALUES ({}, {}, {}, {}, '{}', {}, {})""".format(user['idTarj'], user['idPens'], 'NOW()', 
                                'NOW()', circuit['tbl_configuracion_equipo_posicion'][:1], user['error'], circuit['idtbl_configuracion_equipo']))
            
            if user['error'] == 0:
                if circuit['tbl_configuracion_equipo_posicion'][:1] == 'S': antipass = 0
                querys.append("""UPDATE tbl_tarjetas SET tarj_estatus_antipb = {} 
                                WHERE tarj_id = {}""".format(antipass, user['idTarj']))

            [db['instance'].runQuery(x, db) for x in querys]
            return True
        except Exception as e:
            print(e)
            return False