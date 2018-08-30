from mongoengine import *


class UserModel(Document):
    id = StringField(
        primary_key=True,
    )

    pw = StringField()

    name = StringField()

    phone_number = StringField()
