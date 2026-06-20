from rest_framework import viewsets

from .models import (
    Cliente,
    Veiculo,
    OrdemServico,
    Agendamento,
    Orcamento,
)

from .serializers import (
    ClienteSerializer,
    VeiculoSerializer,
    OrdemServicoSerializer,
    AgendamentoSerializer,
    OrcamentoSerializer,
)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nome')
    serializer_class = ClienteSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all().order_by(
        'marca',
        'modelo',
    )

    serializer_class = VeiculoSerializer


class OrdemServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemServico.objects.all().order_by('-id')
    serializer_class = OrdemServicoSerializer


class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all().order_by(
        'data',
        'hora',
    )

    serializer_class = AgendamentoSerializer
    

class OrcamentoViewSet(viewsets.ModelViewSet):
    queryset = Orcamento.objects.all().order_by('-id')
    serializer_class = OrcamentoSerializer    