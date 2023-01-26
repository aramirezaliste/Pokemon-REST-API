"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/people', methods=['GET'])
def get_all_people():

    return jsonify({
        "Mensaje":"Aca estaran los personajes"
    })

@app.route('/people/<int:id>', methods=['GET'])
def get_id_people(id):

    return jsonify({
        "Mensaje":"Aca esta el personaje por id " + str(id)
    })

@app.route('/planets', methods=['GET'])
def get_all_planets():

    return jsonify({
        "Mensaje":"Aca estaran los planetas"
    })

@app.route('/planets/<int:id>', methods=['GET'])
def get_id_planets(id):

    return jsonify({
        "Mensaje":"Aca esta el planeta por id " + str(id)
    })


@app.route('/users', methods=['GET'])
def handle_hello():

    return jsonify({
        "Mensaje":"Aca estaran los users"
    }), 200

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():

    return jsonify({
        "Mensaje":"Aca estaran todos los favoritos del usuario"
    })

@app.route('/favorite/planet/<int:id>', methods=['POST'])
def post_favorite_planet(id):

    return jsonify({
        "Mensaje":"Añade un planeta favorito con id " + str(id) + " al usuario actual"
    })

@app.route('/favorite/people/<int:id>', methods=['POST'])
def post_favorite_people(id):

    return jsonify({
        "Mensaje":"Añade un personaje favorito con id " + str(id) + " al usuario actual"
    })

@app.route('/favorite/planet/<int:id>', methods=['DELETE'])
def delete_favorite_planet(id):

    return jsonify({
        "Mensaje":"Elimina un planeta favorito con id " + str(id) + " al usuario actual"
    })

@app.route('/favorite/people/<int:id>', methods=['DELETE'])
def delete_favorite_people(id):

    return jsonify({
        "Mensaje":"Elimina un personaje favorito con id " + str(id) + " al usuario actual"
    })


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
