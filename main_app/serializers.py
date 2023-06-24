from rest_framework import serializers, viewsets, permissions
from .models import Restaurant, Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = '__all__'
