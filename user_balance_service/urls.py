from django.contrib import admin
from django.urls import path, include  # Не забудьте импортировать path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Настройка Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="User Balance API",
        default_version='v1',
        description="API для работы с балансом пользователей",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Импорт path исправляет ошибку
    path('api/', include('balance.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
