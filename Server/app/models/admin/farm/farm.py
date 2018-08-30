from mongoengine import *


class FarmModel(document):
    farm_name = StringField()

    farm_phone_number = StringField()

    farm_address = StringField()

    farm_details = StringField()
