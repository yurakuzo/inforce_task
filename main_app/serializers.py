from rest_framework import serializers
from auth_app.models import Vote

from .models import Restaurant, Menu


class MenuSerializer(serializers.ModelSerializer):
    """Basic Menu Serializer"""

    votes = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['title', 'day', 'price', 'description', 'votes']  # Added votes count

    def get_votes(self, obj):
        votes = Vote.objects.filter(chosen_menu=obj)
        return votes.count()


class RestaurantSerializer(serializers.ModelSerializer):
    """Basic Restaurant Serializer"""

    menus = MenuSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = '__all__'
