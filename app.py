from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import pokemon
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Pokemon API. See https://github.com/rxdvd/pokemon-api for more info."

@app.route('/pokemon')
def pokemon_route():
    response = {'message': 'Error: Method Not Allowed'}
    status_code = 405
    if request.method is 'GET':
        response, status_code = pokemon.index(request)
    elif request.method is 'POST':
        response, status_code = pokemon.create(request)
    return jsonify(response), status_code

@app.route('/pokemon/<int:pokemon_id>')
def pokemon_id_route(pokemon_id):
    response = {'message': 'Error: Method Not Allowed'}
    status_code = 405
    if request.method is 'GET':
        response, status_code = pokemon.show(request, pokemon_id)
    elif request.method is 'PATCH':
        response, status_code = pokemon.update(request, pokemon_id)
    elif request.method is 'DELETE':
        response, status_code = pokemon.destroy(request, pokemon_id)
    return jsonify(response), status_code

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Error: {err}'}, 400

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Error: {err}'}, 404

@app.errorhandler(exceptions.MethodNotAllowed)
def handle_405(err):
    return {'message': f'Error: {err}'}, 405

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f'Error: {err}'}, 500
