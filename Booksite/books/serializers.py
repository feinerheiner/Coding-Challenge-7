from rest_framework import serializers
from .models import BookData


class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = BookData
        fields = ['id', 'name', 'author', 'category', 'description', 'rating', 'image']
