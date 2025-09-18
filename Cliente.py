class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, mail=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail

    def __str__(self):
        return (f'ID: {self.id} '
                f'Nombre: {self.nombre} '
                f'Apellido: {self.apellido} '
                f'Mail: {self.mail}')