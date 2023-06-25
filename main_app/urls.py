from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MenuViewSet, RestaurantViewSet, MostVotedMenuList, TodayMenuList

router = DefaultRouter()
router.register(r'menus', MenuViewSet, basename='menus')  # Registering menu-endpoints view set
router.register(r'restaurants', RestaurantViewSet, basename='restaurants')  # Registering restaurant-endpoints view set

urlpatterns = [
    path('', include(router.urls)),  # Added router to urls
    path('menus/today', TodayMenuList.as_view()),  # All menus for today
    path('menus/most_voted', MostVotedMenuList.as_view()),  # Most voted menu for today
]
