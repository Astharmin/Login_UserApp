import os
from mysql.connector import pooling
from mysql.connector import Error
from dotenv import load_dotenv


load_dotenv()

class Conexion:
    DATABASE = os.getenv('DATABASE')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    DB_PORT = os.getenv('DB_PORT')
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'login_app_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool == None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                #print(f'Nombre Pool: {cls.pool.pool_name}')
                #print(f'Tamaño Pool: {cls.pool.pool_size}')
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()

if __name__=='__main__':

    #pool = Conexion.obtener_pool()
    #print(pool)

    cnx1 = Conexion.obtener_conexion()
    print(cnx1)
    Conexion.liberar_conexion(cnx1)

