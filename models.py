from peewee import *
from flask import current_app


def connect_db(path=current_app.config["DATABASE"]):
    return SqliteDatabase(path)


class Driver(Model):
    id = PrimaryKeyField(unique=True)
    code = CharField()
    name = CharField()
    company = CharField()
    result = CharField()

    class Meta:
        database = connect_db()
        order_by = "id"
        db_table = 'drivers'
