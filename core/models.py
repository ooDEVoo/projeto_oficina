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

    foto = models.ImageField(
        upload_to='veiculos/',
        blank=True,
        null=True
    )

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

    servico_realizado = models.TextField(
        blank=True,
        null=True
    )

    valor_pecas = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    valor_mao_obra = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    valor_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    lucro = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Aguardando'
    )

    data_entrada = models.CharField(max_length=20)

    data_previsao = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    data_entrega = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    foto = models.ImageField(
        upload_to='ordens/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'OS #{self.id} - {self.cliente.nome}'


class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('Agendado', 'Agendado'),
        ('Confirmado', 'Confirmado'),
        ('Em andamento', 'Em andamento'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )

    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )

    data = models.CharField(max_length=20)

    hora = models.CharField(max_length=10)

    descricao = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Agendado'
    )

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return (
            f'Agendamento #{self.id} - '
            f'{self.cliente.nome} - '
            f'{self.data} {self.hora}'
        )


class Orcamento(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
        ('Convertido', 'Convertido'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='orcamentos'
    )

    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.CASCADE,
        related_name='orcamentos'
    )

    descricao = models.TextField()

    valor_pecas = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    valor_mao_obra = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    valor_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pendente'
    )

    data_criacao = models.CharField(max_length=20)

    def __str__(self):
        return f'Orçamento #{self.id} - {self.cliente.nome}'