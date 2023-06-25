from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import permission_classes

from .serializers import MenuSerializer, RestaurantSerializer
from .models import Menu, Restaurant
from auth_app.models import Vote

import calendar
from datetime import date

from django.db.models import Count


class MenuViewSet(viewsets.ModelViewSet):
    """Basic Menu ViewSet"""

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class MenuSingleView(generics.RetrieveDestroyAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RestaurantViewSet(viewsets.ModelViewSet):
    """Basic Restaurant ViewSet"""

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@permission_classes([permissions.IsAuthenticatedOrReadOnly])
class TodayMenuList(generics.ListAPIView):
    """List Api View to GET todays menu list"""
    today = calendar.day_name[date.today().weekday()][:2]
    queryset = Menu.objects.filter(day=today)
    serializer_class = MenuSerializer


@permission_classes([permissions.IsAuthenticatedOrReadOnly])
class MostVotedMenuList(generics.ListAPIView):
    """List Api View to GET todays most voted menu list"""

    serializer_class = MenuSerializer

    def get_queryset(self):
        today = calendar.day_name[date.today().weekday()][:2]
        most_voted_menu_id = (
            Vote.objects.filter(chosen_menu__day=today)
                .values('chosen_menu')
                .annotate(the_count=Count('chosen_menu'))
                .order_by('-the_count')
                .values_list('chosen_menu', flat=True)
                .first()
        )
        return Menu.objects.filter(pk=most_voted_menu_id, day=today)
