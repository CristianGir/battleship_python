from flask import Blueprint, Response, json, request, jsonify
from jwt import encode, decode, exceptions
from model.ship import Ship
from service.list_de_service import ListDEService
from model.ship_distribution import ShipDistribution
from util.util import MyEncoder
import time

app_listde = Blueprint("app_listde", __name__)
listde_service = ListDEService()

@app_listde.route("/listde/all")
def get_all_linked():
    return Response(status=200, response=json.dumps(listde_service.get_all_linked(), cls=MyEncoder),
                    mimetype="application/json")

@app_listde.route("/listde/create", methods = ["POST"])
def create_ship():
    request.json
    ship_distribution = ShipDistribution(Ship(request.json))
    return listde_service.add(ship_distribution)

@app_listde.route("/listde/tostar", methods = ["POST"])
def create_ship_to_start():
    request.json
    ship_distribution = ShipDistribution(Ship(request.json))
    return listde_service.add_first(ship_distribution)

@app_listde.route("/listde/load", methods = ["POST"])
def load_ships():
    request.json
    for ship in request.json:
        ship_distribution = ShipDistribution(Ship(ship))
        listde_service.add(ship_distribution)
    return "Barcos cargados con éxito."

@app_listde.route('/listde')
def list():
    token = None
    if 'x-access-token' in request.headers:
        token = request.headers['x-access-token']
        # return 401 if token is not passed
    if not token:
        return jsonify({'message': 'Token is missing !!'}), 401
    response=validate_token(token)
    if not response:
        return Response(status=200,mimetype="application/json",
                    response=json.dumps(listde_service.list(),cls=MyEncoder))
    else:
        return response

@app_listde.route('/login', methods=['POST'])
def login():
    data = request.json
    return token(data)

def token(data):
    llave = "HolaLindos"#getenv('secret')
    token = encode(payload={**data, "duration": int(time.time())}, key=llave, algorithm="HS256")
    return token.encode("UTF-8")

def validate_token(token):
    try:
        decode(token, "HolaLindos", "HS256")
    except exceptions.DecodeError:
        return {"message": "Token inválido"}
    except exceptions.ExpiredSignatureError:
        return {"message": "Token vencido"}

