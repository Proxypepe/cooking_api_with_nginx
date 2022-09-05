from mongoengine import Document
from mongoengine import StringField, ListField, IntField


class Recipe(Document):
    name = StringField(required=True)
    description = StringField(required=True)
    prepare = StringField()
    cook = StringField()
    ingredients = ListField(StringField())
    steps = ListField(StringField())
    file_name = StringField(required=False)
    servings = IntField()
    tags = ListField(StringField(max_length=30))

