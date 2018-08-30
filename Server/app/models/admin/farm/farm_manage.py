from mongoengine import *


class FarmManageModel(document):
    farm_number = IntField()

    farm_user = StringField()

    user_phone_number = StringField()

    farm_period = StringField()

    farm_temperature = DateTimeField()

    farm_fish = GeoJsonBaseField()

    farm_item = GeoJsonBaseField()

    farm_details = StringField()

    all_money = IntField()
