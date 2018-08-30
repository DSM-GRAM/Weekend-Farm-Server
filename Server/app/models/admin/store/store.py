from mongoengine import *


class StoreModel(Document):
    store_product = StringField()

    store_cost = IntField()

    store_Details = StringField()
