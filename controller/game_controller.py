from flask import Blueprint, Response, json, request
from service.game_service import GameService
from util.util import MyEncoder

app_listse = Blueprint("app_listse", __name__)
game_service = GameService()
