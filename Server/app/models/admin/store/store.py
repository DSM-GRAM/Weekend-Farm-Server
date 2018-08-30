from mongoengine import *


class StoreModel(document):
    store_product = StringField()

    store_cost = IntField()

    store_Details = StringField()
