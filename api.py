import json

from flask import jsonify, make_response, config, current_app, Blueprint
from flask_restful import Resource, request
from models import *
from dicttoxml import dicttoxml
from flasgger import swag_from
import collections
collections.Iterable = collections.abc.Iterable


class DriversList(Resource):
    @swag_from('static/drivers.yml')
    def get(self):
        with db:
            database = Driver.select()
            drivers = {}
            for driver in database:
                drivers[driver.code] = [driver.id, driver.name, driver.company, driver.result]

        lis_format = request.args.get('format', default='json')
        order = request.args.get('order', default="desc")
        if lis_format or order:
            if order == "desc":
                drivers = drivers
            elif order == "ask":
                drivers = dict(list(drivers.items())[::-1])

            if lis_format == 'json':
                drivers_json = json.dumps(drivers, indent=2)
                response = make_response(drivers_json)
                response.headers["content-type"] = "application/json"
            elif lis_format == 'xml':
                drivers_xml = dicttoxml(drivers, attr_type=False)

                response = make_response(drivers_xml)
                response.headers['content-type'] = 'application/xml'
            else:
                return drivers
            return response
