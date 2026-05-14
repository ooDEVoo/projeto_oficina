from django.conf import settings
from django.views.static import serve

from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import ClienteViewSet, VeiculoViewSet, OrdemServicoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='clientes')
router.register(r'veiculos', VeiculoViewSet, basename='veiculos')
router.register(r'ordens', OrdemServicoViewSet, basename='ordens')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/', include(router.urls)),

    re_path(
        r'^media/(?P<path>.*)$',
        serve,
        {'document_root': settings.MEDIA_ROOT},
    ),
]