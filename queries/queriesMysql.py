class queriesMysql(object):

    def getTipoEquipo(self, db):
        try:
            query = "SELECT * FROM cat_tipo_equipo WHERE t_equipo_descripcion != 'RFID'"
            return db['instance'].runQuery(query, db)
        except Exception as e:
            print(e)
            return False
    
    def getEquipo(self, db):
        try:
            query = """SELECT tbl_inventario_equipo.inv_eq_id, inv_eq_SQLite_caseta_id, 
                    inv_eq_neg_Id_Usuarios, inv_eq_tipo_equipo_id, inv_eq_ip, Id_Usuarios, Usuario, 
                    t_equipo_id, t_equipo_descripcion
                    FROM tbl_inventario_equipo 
                    JOIN usuarios ON Id_Usuarios = inv_eq_neg_Id_Usuarios
                    JOIN cat_tipo_equipo ON t_equipo_id = inv_eq_tipo_equipo_id"""

            return db['instance'].runQuery(query, db)
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
    
    def getInfoEquipo(self, db):
        try:
            result = {}
            query = """SELECT Id_Movimientos, Fecha_Entrada, Hora_Entrada FROM movimientos 
                    WHERE Id_Movimientos = (SELECT MAX(Id_Movimientos) FROM movimientos)"""
            result['bolE'] = db['instance'].runQuery(query, db)[0]

            query = """SELECT Id_Movimientos, Fecha_Entrada, Hora_entrada, Fecha_Salida, Hora_Salida 
                    FROM movimientos WHERE Id_Movimientos = (SELECT MAX(Id_Movimientos) FROM movimientos 
                                                            WHERE Estatus = 'COBRADO')"""
            result['bolS'] = db['instance'].runQuery(query, db)[0]

            query = """SELECT mope_tarj_id, mope_pnds_id, mope_fecha, mope_hora 
                    FROM tbl_movimientos_pensionados WHERE mope_id = (SELECT MAX(mope_id) 
                                                            FROM tbl_movimientos_pensionados 
                                                            WHERE mope_evento = 'E' AND mope_cea_id_int = 0
                                                            )"""
            result['tarjE'] = db['instance'].runQuery(query, db)[0]

            query = """SELECT mope_tarj_id, mope_pnds_id, mope_fecha, mope_hora 
                    FROM tbl_movimientos_pensionados WHERE mope_id = (SELECT MAX(mope_id) 
                                                            FROM tbl_movimientos_pensionados 
                                                            WHERE mope_evento = 'S' AND mope_cea_id_int = 0
                                                            )"""
            result['tarjS'] = db['instance'].runQuery(query, db)[0]

            return result

        except Exception as e:
            print(e)
            return False