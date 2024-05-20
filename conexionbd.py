# importamos para conectar a postgreSQL
import psycopg2

class conexion():
    #Creamos la funcion para conectar con la base de datos
    def conectar():
        try:
            #Credenciales de conexion y rutas
            connection = psycopg2.connect(
                host = 'localhost',
                user = 'postgres',
                password = 'toor',
                database = 'pruebabd',
                port = '5432'
            )
            print("Conexion Exitosa")
        except Exception as ex:
            print(ex)

        #Creamos el cursor para manipúlar consultas en nuestra base de datos
        cur = connection.cursor()
        print("Conection complete")
        return cur
