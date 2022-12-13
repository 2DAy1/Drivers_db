from flask_restful import Api
import argparse
from flasgger import Swagger
from peewee import SqliteDatabase
from db_drivers import create_db
from api import DriversList
from flask import Flask, g, current_app
from pathlib import Path


def create_app():
    app = Flask(__name__)

    app.config["DATABASE"] = Path(__file__).parent / 'db/drivers.db'
    app.config["FOLDER"] = Path(__file__).parent / "separate folder"

    create_db(app.config["DATABASE"], app.config["FOLDER"])
    Swagger(app)
    create_api(app)
    return app


def create_api(app):
    api = Api(app)
    api.add_resource(DriversList, '/api/v1/report/')
    api.init_app(app)
    return api








if __name__ == '__main__':  # pragma no cover
    create_app().run(debug=True)
