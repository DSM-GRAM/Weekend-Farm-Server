from mongoengine import *
from app.models.farm import FarmModel


class StoreModel(Document):

    name = ReferenceField(
        document_type=FarmModel
    )

    product = StringField()

    cost = IntField()

    details = StringField()