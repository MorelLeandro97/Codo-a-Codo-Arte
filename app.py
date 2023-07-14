# IMPORTAR HERRAMIENTAS
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow

# Crear la app
app = Flask(__name__)

# Usar Cors para dar acceso a las rutas(ebdpoint) desde frontend
CORS(app)

# CONFIGURACIÓN A LA BASE DE DATOS DESDE app
#  (SE LE INFORMA A LA APP DONDE UBICAR LA BASE DE DATOS)
                                                    # //username:password@url/nombre de la base de datos
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/proyecto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 

# COMUNICAR LA APP CON SQLALCHEMY
db = SQLAlchemy(app)

# PERMITIR LA TRANSFORMACIÓN DE DATOS
ma = Marshmallow(app)


# ESTRUCTURA DE LA TABLA producto A PARTIR DE LA CLASE
class Cliente(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    mail = db.Column(db.String(100))
    domicilio = db.Column(db.String(200))
    numero = db.Column(db.Integer)

    def __init__(self,nombre,mail,domicilio,numero):
        self.nombre = nombre
        self.mail = mail
        self.domicilio = domicilio
        self.numero = numero 


# CÓDIGO PARA CREAR LAS TABLAS DEFINIDAS EN LAS CLASES
with app.app_context():
    db.create_all()

# CREAR UNA CLASE  ProductoSchema, DONDE SE DEFINEN LOS CAMPOS DE LA TABLA
class ClienteSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','mail','domicilio','numero')


# DIFERENCIAR CUANDO SE TRANSFORME UN DATO O UNA LISTA DE DATOS
cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)

@app.route('/')
def hello_world():
    return 'Bienvenido a Clientes'

# CREAR LAS RUTAS PARA: productos
# '/productos' ENDPOINT PARA MOSTRAR TODOS LOS PRODUCTOS DISPONIBLES EN LA BASE DE DATOS: GET
# '/productos' ENDPOINT PARA RECIBIR DATOS: POST
# '/productos/<id>' ENDPOINT PARA MOSTRAR UN PRODUCTO POR ID: GET
# '/productos/<id>' ENDPOINT PARA BORRAR UN PRODUCTO POR ID: DELETE
# '/productos/<id>' ENDPOINT PARA MODIFICAR UN PRODUCTO POR ID: PUT

@app.route("/clientes", methods=['GET'])
def get_clientes():
                    # select * from producto
    all_clientes = Cliente.query.all()
    # Almacena un listado de objetos

    return clientes_schema.jsonify(all_clientes)


@app.route("/clientes", methods=['POST'])
def create_clientes():
    """
    Entrada de datos:
    {
        "imagen": "https://picsum.photos/200/300?grayscale",
        "nombre": "MICROONDAS",
        "precio": 50000,
        "stock": 10
}
    """
    nombre = request.json['nombre']
    mail = request.json['mail']
    domicilio = request.json['domicilio']
    numero = request.json['numero']

    new_cliente = Cliente(nombre, mail, domicilio, numero)
    db.session.add(new_cliente)
    db.session.commit()

    return cliente_schema.jsonify(new_cliente)


@app.route("/clientes/<id>", methods=['GET'])
def get_cliente(id):
    cliente = Cliente.query.get(id)

    return cliente_schema.jsonify(cliente)


@app.route('/clientes/<id>',methods=['DELETE'])
def delete_cliente(id):
    # Consultar por id, a la clase Producto.
    #  Se hace una consulta (query) para obtener (get) un registro por id
    cliente=Cliente.query.get(id)
    
    # A partir de db y la sesión establecida con la base de datos borrar 
    # el producto.
    # Se guardan lo cambios con commit
    db.session.delete(cliente)
    db.session.commit()

    return cliente_schema.jsonify(cliente)
    

@app.route('/clientes/<id>',methods=['PUT'])
def update_cliente(id):
    # Consultar por id, a la clase Producto.
    #  Se hace una consulta (query) para obtener (get) un registro por id
    cliente=Cliente.query.get(id)
 
    #  Recibir los datos a modificar
    nombre=request.json['nombre']
    mail=request.json['mail']
    domicilio=request.json['domicilio']
    numero=request.json['numero']

    # Del objeto resultante de la consulta modificar los valores  
    cliente.nombre=nombre
    cliente.mail=mail
    cliente.domicilio=domicilio
    cliente.numero=numero
#  Guardar los cambios
    db.session.commit()
# Para ello, usar el objeto producto_schema para que convierta con                     # jsonify el dato recién eliminado que son objetos a JSON  
    return cliente_schema.jsonify(cliente)



# BLOQUE PRINCIPAL 
if __name__=='__main__':
    app.run(debug=True)