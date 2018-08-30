from mongoengine import *


class StoreApplyModel(Document):
    product_name = StringField()

    product_number = IntField()

    product_cost = IntField()
