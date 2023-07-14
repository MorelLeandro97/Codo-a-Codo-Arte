from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://ArteCodoaCodo:Arte12345@ArteCodoaCodo.mysql.pythonanywhere-services.com/ArteCodoaCodo$default'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

ma = Marshmallow(app)

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

with app.app_context():
    db.create_all()

class ClienteSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','mail','domicilio','numero')

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)

@app.route('/')
def hello_world():
    return 'Bienvenido a Clientes'

@app.route("/clientes", methods=['GET'])
def get_clientes():
    all_clientes = Cliente.query.all()

    return clientes_schema.jsonify(all_clientes)


@app.route("/clientes", methods=['POST'])
def create_clientes():
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
    cliente=Cliente.query.get(id)

    db.session.delete(cliente)
    db.session.commit()

    return cliente_schema.jsonify(cliente)


@app.route('/clientes/<id>',methods=['PUT'])
def update_cliente(id):
    cliente=Cliente.query.get(id)

    nombre=request.json['nombre']
    mail=request.json['mail']
    domicilio=request.json['domicilio']
    numero=request.json['numero']

    cliente.nombre=nombre
    cliente.mail=mail
    cliente.domicilio=domicilio
    cliente.numero=numero
    db.session.commit()
    return cliente_schema.jsonify(cliente)

if __name__=='__main__':
    app.run(debug=True)