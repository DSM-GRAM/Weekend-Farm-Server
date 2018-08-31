from mongoengine import *
from app.models.farm import FarmModel
from app.models.user import UserModel


class ApplyModel(Document):
    farm = ReferenceField(
        document_type=FarmModel
    )

    user = ReferenceField(
        document_type=UserModel
    )

    period = StringField()

    details = StringField()

    use_farm_num = IntField()

    use_farm_fish = StringField()

    use_amount = IntField()