from rest_framework import serializers
from .models import Cliente, Veiculo, OrdemServico


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class VeiculoSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)

    class Meta:
        model = Veiculo
        fields = '__all__'


class OrdemServicoSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)
    veiculo_nome = serializers.SerializerMethodField()
    veiculo_placa = serializers.CharField(source='veiculo.placa', read_only=True)

    class Meta:
        model = OrdemServico
        fields = '__all__'

    def get_veiculo_nome(self, obj):
        return f'{obj.veiculo.marca} {obj.veiculo.modelo}'