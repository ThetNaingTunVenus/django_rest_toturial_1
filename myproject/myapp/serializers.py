from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','author','email','date']


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    role = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


