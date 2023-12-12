'''
API Rest con Python y MySQL, usando conexión por medio de XAMPP
'''

from flask import Flask, jsonify
# Para definir la conexión a la base de datos
from flask_sqlalchemy import SQLAlchemy
# Para definir los esquemas
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/bdpythonapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Modelando la base de datos (Columnas)
class Categoria(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_nom = db.Column(db.String(100))
    cat_desp = db.Column(db.String(100))

    def __init__(self, cat_nom, cat_desp):
        self.cat_nom = cat_nom
        self.cat_desp = cat_desp

# Para abrir y cerrar la conexión a la base de datos, actualiza la base de datos y agrega las columnas
with app.app_context():
    db.create_all()

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('cat_id', 'cat_nom', 'cat_desp')

# Con 1 sola respuesta
categoria_schema = CategoriaSchema()

# Con muchas respuestas
categorias_schema = CategoriaSchema(many=True)

# GET
@app.route('/categoria', methods=['GET'])
def get_categorias():
    all_categorias = Categoria.query.all()
    result = categorias_schema.dump(all_categorias)
    return jsonify(result)

@app.route('/', methods=['GET'])
def index():
    # Retorna un mensaje en formato Json
    return jsonify({'Mensaje':'Ingreso API por Flask'})

if __name__ == '__main__':
    # Ejecución de la aplicación con el debug para compilar con la app en uso
    app.run(debug=True)
    



