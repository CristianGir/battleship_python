from flask import Flask, json, Response

from controller.list_de_controller import app_listde

app = Flask(__name__)
app.register_blueprint(app_listde)

if __name__ == '__main__':
    app.run()
