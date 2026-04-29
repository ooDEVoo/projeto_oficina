from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import ClienteViewSet, VeiculoViewSet, OrdemServicoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='clientes')
router.register(r'veiculos', VeiculoViewSet, basename='veiculos')
router.register(r'ordens', OrdemServicoViewSet, basename='ordens')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]