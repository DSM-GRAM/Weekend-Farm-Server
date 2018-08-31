from mongoengine import *
from app.models.farm import FarmModel


class StoreModel(Document):
    user = ReferenceField(
        document_type=FarmModel
    )

    itemName = StringField()

    itemNum = IntField()

    money = IntField()

    details = StringField()
