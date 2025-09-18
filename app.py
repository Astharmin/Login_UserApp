from flask import Flask, render_template, redirect, url_for

from Cliente import Cliente
from Cliente_DAO import ClienteDAO
from cliente_form import ClienteForm

app = Flask(__name__)
titulo_app = 'Login App'

app.config['SECRET_KEY'] = 'llave_secreta'

@app.route('/') #url: http://localhost:5000/
@app.route('/index.html') #url : http://localhost:500/index.html

def inicio():
    app.logger.debug('Entramos al path de inicio /')

    clientes_db = ClienteDAO.seleccionar()
    cliente = Cliente()
    cliente_form = ClienteForm(obj=cliente)

    return render_template('index.html',
                           titulo=titulo_app,
                           clientes=clientes_db,
                           forma=cliente_form)

@app.route('/guardar', methods=['POST'])
def guardar():
    cliente = Cliente()
    cliente_form = ClienteForm(obj=cliente)

    if cliente_form.validate_on_submit():
        cliente_form.populate_obj(cliente)
        ClienteDAO.insertar(cliente)

    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)