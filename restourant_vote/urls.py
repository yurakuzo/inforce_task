from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('restaurant-api/', include('main_app.urls')),
    path('auth/', include('auth_app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
