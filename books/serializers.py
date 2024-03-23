from typing import Optional
from books.models import Book, Article
from fastapi_auth.tortoise_models.serializers import ModelSerializer


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "name",)


class BookSerializer(ModelSerializer):
    author: str
    article: Optional[ArticleSerializer.response_schema()] = ArticleSerializer

    async def get_author(self, instance: Book) -> str:
        user = await instance.author
        return user.email

    async def get_article(self, instance: Book) -> Optional[Article]:
        article = await instance.article
        return article

    class Meta:
        model = Book
        fields = "__all__"
