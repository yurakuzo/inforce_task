from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import VoteViewSet, EmployeeRegisterViewSet, EmployeeViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'votes', VoteViewSet, basename='votes')
router.register(r'employees', EmployeeViewSet, basename='employees')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', EmployeeRegisterViewSet.as_view(), name='register'),
]
