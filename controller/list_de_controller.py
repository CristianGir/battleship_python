from flask import Blueprint, Response, json, request

from model.ship import Ship
from service.list_de_service import ListDEService
from model.ship_distribution import Ship_Distribution
from util.util import MyEncoder

app_listde = Blueprint("app_listde", __name__)
listde_service = ListDEService()

@app_listde.route("/listde/all")
def get_all_linked():
    return Response(status=200, response=json.dumps(listde_service.get_all_linked(), cls=MyEncoder),
                    mimetype="application/json")

@app_listde.route("/listde/create", methods = ["POST"])
def create_ship():
    request.json
    ship_distribution = Ship_Distribution(Ship(request.json))
    return listde_service.add(ship_distribution)

@app_listde.route("/listde/tostar", methods = ["POST"])
def create_ship_to_start():
    request.json
    ship_distribution = Ship_Distribution(Ship(request.json))
    return listde_service.add_first(ship_distribution)

@app_listde.route("/listde/load", methods = ["POST"])
def load_ships():
    request.json
    for ship in request.json:
        ship_distribution = Ship_Distribution(Ship(ship))
        listde_service.add(ship_distribution)
    return "Barcos cargadas con éxito."
