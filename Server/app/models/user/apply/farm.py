from mongoengine import *


class MiniFarmApplyModel(EmbeddedDocument):
    mini_farm_number = IntField()

    mini_farm_fish_kind = ListField(null=True)

    mini_farm_fish_number = IntField()


class FarmApplyModel(Document):
    user_name = StringField()

    user_phone_number = StringField()

    period = DateTimeField()

    details = StringField()

    mini_farm_list = ListField(
        EmbeddedDocument(MiniFarmApplyModel)
    )

