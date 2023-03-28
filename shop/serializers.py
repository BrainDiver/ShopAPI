from rest_framework import serializers
from .models import Category, Product, Costumer

class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Costumer
        fields= '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= '__all__'

#I can make serializer with default class ModelSerializer
#but in this task  i want make my own serializer
#based on the parrent class Serializer
class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    name = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class CategoryProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.FloatField()
    category_id = serializers.IntegerField()
    
