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

    args = create_parser()
    create_db(args.folder, args.database)

    Swagger(app)
    create_api(app)
    return app


def create_api(app):
    api = Api(app)
    api.add_resource(DriversList, '/api/v1/report/')
    api.init_app(app)
    return api


def create_parser(string=None):
    parser = argparse.ArgumentParser(description='Get drivers statistic')
    parser.add_argument('--folder', metavar='', help='Specify where the files are located', nargs='?',
                        default=current_app.config["FOLDER"])
    parser.add_argument('--database', metavar='', help='Specify where the database are located',
                        default=current_app.config["DATABASE"], nargs='?')
    return parser.parse_args(string)





if __name__ == '__main__':  # pragma no cover
    create_app().run(debug=True)
