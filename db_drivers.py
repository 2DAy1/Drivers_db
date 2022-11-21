import argparse
from flask import current_app
from models import connect_db, Driver
from report_of_monaco_2018_racing_dan import report





def get_drivers(path=None):
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


def create_db(folder, database):

    db = connect_db(database)
    with db:
        db.create_tables([Driver])

        drivers_dict = get_drivers(folder)

        drivers_list = []
        for code in drivers_dict:
            driver = drivers_dict[code]
            driver = dict(code=code,
                          name=driver['name'],
                          company=driver['company'],
                          result=driver['result'])
            drivers_list.append(driver)
        Driver.insert_many(drivers_list).execute()

    return db






# def get_db():
#     if not hasattr()