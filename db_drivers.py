import argparse
import sqlite3
from flask import Flask, g, current_app
from models import *
from report_of_monaco_2018_racing_dan import report

def create_parser(data, folder,string=None):
    parser = argparse.ArgumentParser(description='Get drivers statistic')
    parser.add_argument('--folder', metavar='', help='Specify where the files are located', nargs='?',
                        default=folder)
    parser.add_argument('--database', metavar='', help='Specify where the database are located',
                        default=data, nargs='?')
    return parser.parse_args(string)

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
    return drivers_list


def create_db(data, folder):
    args = create_parser(data,folder)
    data = args.database
    folder = args.folder

    init_db(data)
    with database:
        database.create_tables([Driver])
        Driver.insert_many(get_driver_list(folder)).execute()












