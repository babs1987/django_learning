from django.db import models
from django.db.models import base
from django.db.models import fields


# Create your models here.


class Author(base.Model):
    first_name = fields.CharField(max_length=30)
    last_name = fields.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(base.Model):
    title = fields.CharField(max_length=50)
    # каскад обеспечивает удаление
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.title}'

class Publisher(base.Model):
    name = fields.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    books = models.ManyToManyField(Book)


# после каждого изменения можели нужно делать миграцию
# py manage.py makemigrations main
# (опционально) компиляция SQL кода в отдельный файл
# py manage.py sqlmigrate %имя приложения% %номер миграции% >%имя приложение% \migrations\%номер миграции%.sql
# применить миграции py manage.py migrate

