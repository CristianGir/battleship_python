from flask import Blueprint, Response, json, request
from service.list_de_service import ListDEService
from util.util import MyEncoder

app_listse = Blueprint("app_listse", __name__)
list_de_service = ListDEService()
