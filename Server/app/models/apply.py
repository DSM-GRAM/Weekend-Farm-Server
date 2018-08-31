from mongoengine import *
from app.models.farm import FarmModel
from app.models.user import UserModel


class RoomModel(EmbeddedDocument):
    rNum = IntField()

    rFishKind = IntField()

    rAmount = IntField()


class ApplyModel(Document):
    farm = ReferenceField(
        document_type=FarmModel
    )

    user = ReferenceField(
        document_type=UserModel
    )

    phoneNum = StringField()

    applyDate = StringField()

    message = StringField()

    roominfo = EmbeddedDocumentListField(
        document_type=RoomModel
    )


class ItemApplyModel(Document):
    itemNum = IntField()

    itemName = StringField()

    money = IntField()