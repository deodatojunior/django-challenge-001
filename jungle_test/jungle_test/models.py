import uuid
from django.db import models

class Author(models.Model):
    id = models.UUIDField("id", primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("name", max_length=155)
    picture = models.URLField("picture")

class Article(models.Model):
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    category = models.CharField("category", max_length=120)
    title = models.CharField("title", max_length=255)
    summary = models.CharField("Summary", max_length=300)
    firstParagraph = models.CharField("First paragraph", max_length=355)
    body = models.TextField("body")
