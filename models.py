from peewee import *


database = SqliteDatabase(None)


class Driver(Model):
    id = PrimaryKeyField(unique=True)
    code = CharField()
    name = CharField()
    company = CharField()
    result = CharField()

    class Meta:
        database = database
        order_by = "id"
        db_table = 'drivers'




def init_db(path):
    database.init(path)
