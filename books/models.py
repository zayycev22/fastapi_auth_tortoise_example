from fastapi_auth_tortoise_models import ExModel
from tortoise import fields
from auth.models import User


class Article(ExModel):
    name = fields.CharField(max_length=100)
    book = fields.OneToOneField("models.Book", on_delete=fields.CASCADE, related_name="article")

    class Meta:
        table = "article"


class Book(ExModel):
    name = fields.CharField(max_length=100, null=False)
    author: fields.ForeignKeyRelation[User] = fields.ForeignKeyField("models.User", related_name="books",
                                                                     on_delete=fields.CASCADE)
    time_created = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "book"
