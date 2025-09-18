from Cliente import Cliente
from Conexion import Conexion


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, mail) VALUES(%s,%s,%s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, mail=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()

            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0],registro[1],
                                  registro[2],registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre,
                       cliente.apellido,
                       cliente.mail)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al Insertar: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido,
                       cliente.mail, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f' Ocurrio un Error al actualizar {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
            
        except Exception as e:
            print(f'Ocurrio un Error al eliminar: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    # Prueba Insertar
    # cliente1 = Cliente(nombre='Prueba',apellido='Prueba', mail='pprueba@mail.com')
    # clienes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes Insertados: {clienes_insertados}')

    # Prueba Seleccionar
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

    # Prueba Actualizar
    # cliente_actualizar = Cliente(1, 'Daniel','Torres','dtorres@mail.com')
    # clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes Actualizados: {clientes_actualizados}')

    # Prueba Eliminar
    # cliente_eliminar = Cliente(id=5)
    # clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    # print(f'Clientes Eliminados: {clientes_eliminados}')