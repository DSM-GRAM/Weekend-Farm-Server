from mongoengine import *
from app.models.admin import AdminModel


class MiniFarmFishModel(EmbeddedDocument):
    kind = StringField()
    amount = IntField()


class MiniFarmModel(EmbeddedDocument):
    user_name = ReferenceField(
        document_type=AdminModel,
        default=None
    )

    user_phone_number = ReferenceField(
        document_type=AdminModel,
        default=None
    )

    period = StringField(
        default=None
    )

    temperature = IntField(
        default=None
    )

    farm_number = IntField()

    farm_cost = IntField()

    farm_fish_max = IntField()

    fish_kind = EmbeddedDocumentListField(
        document_type=MiniFarmFishModel
    )

    details = StringField()


class FarmModel(Document):
    farm_name = StringField()

    farm_hostname = ReferenceField(
        document_type=AdminModel
    )

    farm_phone_number = StringField()

    farm_address = StringField()

    farm_details = StringField()

    farm_address_do = StringField()

    mini_farms = EmbeddedDocumentListField(
        document_type=MiniFarmModel
    )