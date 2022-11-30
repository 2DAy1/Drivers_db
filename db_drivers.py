import sqlite3
from flask import Flask, g, current_app
from models import *
from report_of_monaco_2018_racing_dan import report


def get_drivers_dict(path):
    drivers = {}
    for driver in report.create_drivers(path):
        drivers[driver.code] = {
            "number":
                driver.number,
            "name":
                driver.name,
            "company":
                driver.company,
            "result":
                driver.result
        }
    return drivers


def get_driver_list(folder):
    drivers_dict = get_drivers_dict(folder)
    drivers_list = []
    for code in drivers_dict:
        driver = drivers_dict[code]
        driver = dict(code=code,
                      name=driver['name'],
                      company=driver['company'],
                      result=driver['result'])
        drivers_list.append(driver)


def create_db(data, folder):
    init_db(data)
    with database:
        database.create_tables([Driver])
        with database.atomic():
            Driver.bulk_create(get_driver_list(folder)).execute()












