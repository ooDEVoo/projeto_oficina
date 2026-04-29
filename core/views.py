from rest_framework import viewsets
from .models import Cliente, Veiculo, OrdemServico
from .serializers import (
    ClienteSerializer,
    VeiculoSerializer,
    OrdemServicoSerializer,
)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nome')
    serializer_class = ClienteSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all().order_by('marca', 'modelo')
    serializer_class = VeiculoSerializer


class OrdemServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemServico.objects.all().order_by('-id')
    serializer_class = OrdemServicoSerializer