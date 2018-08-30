from mongoengine import *


class UsedFarmModel(document):
    farm_number = IntField()

    farm_cost = IntField()

    fish_max = IntField()

    temperature = IntField()
