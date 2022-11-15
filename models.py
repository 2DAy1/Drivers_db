from peewee import *
from pathlib import Path


db = SqliteDatabase('db/drivers.db')


class Driver(Model):
    id = PrimaryKeyField(unique=True)
    code = CharField()
    name = CharField()
    company = CharField()
    result = CharField()

    class Meta:
        database = db
        order_by = "id"
        db_table = 'drivers'

