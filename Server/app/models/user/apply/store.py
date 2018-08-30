from mongoengine import *


class StoreApplyModel(document):
    product_name = StringField()

    product_number = IntField()

    product_cost = IntField()
