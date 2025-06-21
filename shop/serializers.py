from rest_framework import serializers
from .models import Товар, Производитель, Категория, Материал, Покупатель
from django.contrib.auth.models import User

class ПроизводительSerializer(serializers.ModelSerializer):
    class Meta:
        model = Производитель
        fields = ['id', 'название', 'страна', 'сайт']

class КатегорияSerializer(serializers.ModelSerializer):
    class Meta:
        model = Категория
        fields = ['id', 'название']

class МатериалSerializer(serializers.ModelSerializer):
    class Meta:
        model = Материал
        fields = ['id', 'название', 'описание', 'экологичный']

class ТоварSerializer(serializers.ModelSerializer):
    производитель = ПроизводительSerializer(read_only=True)
    категория = КатегорияSerializer(read_only=True)
    материалы = МатериалSerializer(many=True, read_only=True)
    
    class Meta:
        model = Товар
        fields = [
            'id', 'название', 'описание', 'цена', 'изображение', 
            'тип', 'производитель', 'категория', 'материалы'
        ]

class ПокупательSerializer(serializers.ModelSerializer):
    пользователь = serializers.StringRelatedField()
    
    class Meta:
        model = Покупатель
        fields = ['id', 'пользователь', 'телефон']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        read_only_fields = ['id'] 