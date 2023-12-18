from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Modelo para representar os funcionários
class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)  # Pode ser estendido conforme necessário
    veiculo = models.ForeignKey('Veiculo', on_delete=models.SET_NULL, null=True, blank=True, related_name='funcionarios')

    def __str__(self):
        return self.user.username
    
# Modelo para representar os veículos
class Veiculo(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='veiculos')
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=20)
    placa = models.CharField(max_length=15)
    capacidade = models.IntegerField()
    
    def __str__(self):
        return f"Modelo: {self.modelo}|Cor: {self.cor}"

    
# Modelo para representar as caronas
class Carona(models.Model):
    motorista = models.ForeignKey(Funcionario, related_name='caronas_oferecidas', on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True, blank=True, related_name='caronas', verbose_name=u"Veículo")
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    horario = models.DateTimeField(verbose_name=u"Horário")
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField(blank=True, verbose_name="Descrição")
    vagas_disponiveis = models.PositiveIntegerField()

    def __str__(self):
        return f"Carona de {self.motorista.user.username} - {self.origem} para {self.destino}"

# Modelo para representar as inscrições de carona
class InscricaoCarona(models.Model):
    carona = models.ForeignKey(Carona, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=[('P', 'Pendente'), ('A', 'Aceita'), ('R', 'Recusada')])

    def __str__(self):
        return f"Inscrição de {self.funcionario.user.username} na carona de {self.carona.motorista.user.username}"

