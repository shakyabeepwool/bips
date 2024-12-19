from rest_framework import serializers
from . import models

class BooksSerializer(serializers.ModelSerializers):
    class Meta:
        models = models.BookModel
        fields = "__all__"