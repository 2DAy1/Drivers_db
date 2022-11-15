import sqlite3
from pathlib import Path

from models import db, Driver
from drivers import get_drivers

with db:
    db.create_tables([Driver])
    drivers_dict = get_drivers()
    drivers_list = []
    for code in drivers_dict:
        driver = drivers_dict[code]
        driver = dict(code=code,
                      name=driver['name'],
                      company=driver['company'],
                      result=driver['result'])
        drivers_list.append(driver)
    Driver.insert_many(drivers_list).execute()
