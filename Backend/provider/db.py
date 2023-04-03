import mysql.connector

class Database:
    def __init__(self):
        self.mydb = None
        self.mycursor = None

    def connect(self):
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

        # Inicia la transacción
        self.mycursor.execute("START TRANSACTION")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # Si se produce una excepción, se llama al método rollback para deshacer los cambios
            self.mydb.rollback()
            print("Rollback realizado")
        else:
            # Si todo está bien, se confirma la transacción
            self.mydb.commit()
            print("Transacción confirmada")

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
    
    def disconnect(self):
        if self.mydb.is_connected():
            self.mycursor.close()
            self.mydb.close()
            print("Conexión a la base de datos cerrada")