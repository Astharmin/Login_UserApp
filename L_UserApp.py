from Cliente import Cliente
from Cliente_DAO import ClienteDAO

print(' Clientes de la App '.center(30,'-'))
opcion = None
while opcion != 5:
    print('''Menu:
    
    1.- Listar
    2.- Agregar
    3.- Actualizar
    4.- Eliminar
    5.- Salir    
    ''')

    opcion = int(input('Que quieres hacer? (1-5):\n'))
    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print('Listado de Clientes'.center(30, '-'))
        for cliente in clientes:
            print(cliente)
        print()

    elif opcion == 2:
        nombre_var = input('Escribe el nombre:')
        apellido_var = input('Escribe el apellido:')
        mail_var = input('Escribe el imail:')

        cliente = Cliente(nombre=nombre_var,
                          apellido=apellido_var,
                          mail=mail_var)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes Insertados: {clientes_insertados}\n')

    elif opcion == 3:
        id_cliente_var = int(input('ID del Clinete?:\n'))
        nombre_var = input('Escribe el nombre:')
        apellido_var = input('Escribe el apellido:')
        mail_var = input('Escribe el imail:')

        cliente = Cliente(id_cliente_var, nombre_var,
                          apellido_var, mail_var)
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        print(f'Clientes Actualizados: {clientes_actualizados}\n')

    elif opcion == 4:
        id_cliente_var = int(input('ID del Clinete?:\n'))
        cliente = Cliente(id=id_cliente_var)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f'Clientes Eliminados: {clientes_eliminados}\n')

    else:
        print('Saliendo de la App...')