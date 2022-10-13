from rest_framework import serializers
from .models import News


class NewsSerializes(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
