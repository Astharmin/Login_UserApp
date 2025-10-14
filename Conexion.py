import os
from mysql.connector import pooling
from mysql.connector import Error
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Conexion:
    DATABASE = os.getenv('DB_NAME')
    USERNAME = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    DB_PORT = os.getenv('DB_PORT')
    HOST = os.getenv('DB_HOST', 'localhost')
    POOL_SIZE = int(os.getenv('POOL_SIZE', 5))
    POOL_NAME = os.getenv('POOL_NAME', 'login_app_pool')
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
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
                return cls.pool
            except Error as e:
                print(f'Error al obtener pool: {e}')
                return None
        return cls.pool

    @classmethod
    def obtener_conexion(cls):
        pool = cls.obtener_pool()
        if pool:
            return pool.get_connection()
        return None

    @classmethod
    def liberar_conexion(cls, conexion):
        if conexion:
            conexion.close()