"""taos_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import silk

from people.views import PersonViewSet
from dealerships.views import AutoViewSet, DealershipViewSet

router = DefaultRouter()

# Viewset routers
router.register(r"api/people", PersonViewSet, basename="person")
router.register(r"api/autos", AutoViewSet, basename="auto")
router.register(r"api/dealerships", DealershipViewSet, basename="dealers")

# Swagger Settings
schema_view = get_schema_view(
    openapi.Info(
        title='Taos DRF API',
        default_version='v1',
        description='Taos DRF Course test API'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r'login/', auth_views.LoginView.as_view(), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(), name='logout'),
    path(r'api_docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path(r'profiler/', include('silk.urls'), name='profiler')
] + router.urls
