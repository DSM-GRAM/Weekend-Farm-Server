from mongoengine import *
from app.models.user import UserModel


class StoreModel(Document):
    user = ReferenceField(
        document_type=UserModel
    )

    itemName = StringField()

    itemNum = IntField()

    money = IntField()

    details = StringField()
