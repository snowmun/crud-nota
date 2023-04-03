import mysql.connector

class Database:
    def __init__(self):
        self.mydb = None
        self.mycursor = None

    def connect(self):
        # Se crea una conexión con la base de datos utilizando las credenciales proporcionadas
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="secreta12",
            database="nota_test"
        )

        # Se crea un cursor para ejecutar las consultas
        self.mycursor = self.mydb.cursor()

        if self.mydb.is_connected():
            print("Conexión exitosa a la base de datos")
        else:
            print("Error al conectar a la base de datos")

    def disconnect(self):
        if self.mydb.is_connected():
            self.mycursor.close()
            self.mydb.close()
            print("Conexión a la base de datos cerrada")

    def query(self, sql, params=None):
        # Se ejecuta una consulta con los parámetros especificados
        if params:
            self.mycursor.execute(sql, params)
        else:
            self.mycursor.execute(sql)
        
        return self.mycursor.fetchall()

    def commit(self):
        self.mydb.commit()
