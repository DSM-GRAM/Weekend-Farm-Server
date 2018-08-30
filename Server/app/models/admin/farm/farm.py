from mongoengine import *


class MiniFarmModel(EmbeddedDocument)
    minifarm_num = IntField()
    minifarm_fish_kind = ListField(null=True)
    minifarm_fish_number = IntField()


class FarmModel(Document):
    farm_name = StringField()

    farm_hostname = StringField()

    farm_phone_number = StringField()

    farm_address = StringField()

    farm_details = StringField()

    farm_address_do = StringField()

    minifarm = ListField()
