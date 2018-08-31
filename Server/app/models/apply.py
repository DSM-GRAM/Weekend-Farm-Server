from mongoengine import *
from app.models.farm import FarmModel
from app.models.user import UserModel


class ApplyModel(Document):
    farm_name = ReferenceField(
        document_type=FarmModel
    )

    applier_phone_number = ReferenceField(
        document_type=UserModel
    )

    period = ReferenceField(
        document_type=FarmModel
    )

    details = StringField()

    use_farm_num = IntField()

    use_farm_fish = StringField()

    use_amount = IntField()