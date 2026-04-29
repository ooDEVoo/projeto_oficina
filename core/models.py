from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cpf_cnpj = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='veiculos'
    )
    placa = models.CharField(max_length=20)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.CharField(max_length=10, blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    quilometragem = models.CharField(max_length=50, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.placa}'


class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('Aguardando', 'Aguardando'),
        ('Em andamento', 'Em andamento'),
        ('Concluído', 'Concluído'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='ordens'
    )
    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.CASCADE,
        related_name='ordens'
    )
    descricao_problema = models.TextField()
    servico_realizado = models.TextField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Aguardando'
    )
    data_entrada = models.CharField(max_length=20)
    data_previsao = models.CharField(max_length=20, blank=True, null=True)
    data_entrega = models.CharField(max_length=20, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'OS #{self.id} - {self.cliente.nome}'