import json

from flask import jsonify, make_response, config, current_app, Blueprint
from flask_restful import Resource, request
from models import connect_db, Driver
from dicttoxml import dicttoxml
from flasgger import swag_from
import collections

collections.Iterable = collections.abc.Iterable


def get_drivers(order):
    db = connect_db()

    with db:
        database = Driver.select().order_by(Driver.id)
        if order == 'ask':
            database = Driver.select().order_by(Driver.id[::-1])
        drivers = {}
        for driver in database[:-1]:
            drivers[driver.code] = [driver.id, driver.name, driver.company, driver.result]
    return drivers


class DriversList(Resource):

    @swag_from('static/drivers.yml')
    def get(self):

        lis_format = request.args.get('format', default='json')
        order = request.args.get('order', default="desc")

        if lis_format or order:

            if order == "desc" or order == "ask":
                drivers = get_drivers(order)
            else:
                raise ValueError("order != desc or order != ask")

            # get format
            drivers_json = json.dumps(drivers, indent=2)
            response = make_response(drivers_json)
            response.headers["content-type"] = "application/json"
            if lis_format == 'xml':
                drivers_xml = dicttoxml(drivers, attr_type=False)
                response = make_response(drivers_xml)
                response.headers['content-type'] = 'application/xml'
            elif lis_format != 'json':
                raise ValueError("format != json or xml")

            return response
