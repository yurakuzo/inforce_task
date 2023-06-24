from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MenuViewSet, RestaurantViewSet, MostVotedMenuList, TodayMenuList, MenuSingleView

router = DefaultRouter()
router.register(r'menus', MenuViewSet)
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('menus/<int:pk>', MenuSingleView.as_view()),
    path('menus/today', TodayMenuList.as_view()),
    path('menus/most_voted', MostVotedMenuList.as_view()),
]
