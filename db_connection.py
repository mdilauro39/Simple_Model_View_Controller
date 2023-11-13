# -*- coding: utf-8 *-*
import sqlite3
import time


class DBConn:

    def __init__(self, db_file="tutorial.db"):
        self.db_file = db_file
        self.conectar()
        self.abrir_cursor()
        if self.detectar_tabla() is False:
            self.crear_tabla()
            self.cerrar_cursor

    def conectar(self):
        """Crear una conexión con la base de datos"""
        self.dbconn = sqlite3.connect(self.db_file)

    def abrir_cursor(self):
        """Abrir un cursor"""
        self.cursor = self.dbconn.cursor()

    def crear_tabla(self):
        self.cursor.execute("CREATE TABLE persona(idpersona INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT, apellido TEXT,genero TEXT,dni INTEGER,timestamp DATE DEFAULT (datetime('now','localtime')),desde TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);")

    def ejecutar_consulta(self, query, values=''):
        """Ejecutar una consulta"""
        if values != '':
            print("sinvalues")
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

    def traer_datos(self):
        """Traer todos los registros"""
        self.rows = self.cursor.fetchall()

    def send_commit(self, query):
        """Enviar commit a la base de datos"""
        sql = query.lower()
        es_lectura = sql.count('select')
        if es_lectura < 1:
            self.dbconn.commit()

    def cerrar_cursor(self):
        """Cerrar cursor"""
        self.cursor.close()
    
    def detectar_tabla(self):
        try:
            res = self.cursor.execute("SELECT name FROM sqlite_master")
            if not res.fetchone():
                return False
            else:
                return True
        except sqlite3.DatabaseError as e:
            print(e)
            return False 


    def ejecutar(self, query, values=''):
        """Compilar todos los procesos"""
        # ejecuta todo el proceso solo si las propiedades han sido definidas
        print(query)
        print(values)
        if (self.db_file and query):
            self.conectar()
            self.abrir_cursor()
            self.ejecutar_consulta(query, values)
            self.send_commit(query)
            self.traer_datos()
            self.cerrar_cursor()
            return self.rows
    
   