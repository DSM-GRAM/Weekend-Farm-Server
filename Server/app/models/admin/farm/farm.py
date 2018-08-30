from mongoengine import *


class FarmModel(Document):
    farm_name = StringField()

    farm_hostname = StringField()

    farm_phone_number = StringField()

    farm_address = StringField()

    farm_details = StringField()

    farm_address_do = StringField()

    mini_farms = ListField()
