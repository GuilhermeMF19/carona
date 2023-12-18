from django.test import TestCase
from django.urls import reverse
from .models import Carona, Veiculo, Funcionario, InscricaoCarona
from django.contrib.auth.models import User

class HomeViewTest(TestCase):
    def test_home_view_status_code(self):
        # Cria um usuário de teste
        user = User.objects.create_user(username='testuser', password='testpassword')
        # Cria um objeto Funcionario associado a esse usuário
        funcionario = Funcionario.objects.create(user=user)
        # Faz login com o usuário de teste
        self.client.login(username='testuser', password='testpassword')
        # Acessa a página inicial
        response = self.client.get(reverse('home'))
        # Verifica se a resposta retorna um código de status HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_home_view_status_code2(self):
        # Cria um usuário de teste
        user = User.objects.create_user(username='testuser', password='testpassword')
        # Cria um objeto Funcionario associado a esse usuário
        funcionario = Funcionario.objects.create(user=user)
        # Faz login com o usuário de teste
        self.client.login(username='testuser')
        # Acessa a página inicial
        response = self.client.get(reverse('home'))
        # Verifica se a resposta retorna um código de status HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_home_view_template(self):
        # Cria um usuário de teste
        user = User.objects.create_user(username='testuser', password='testpassword')
        # Cria um objeto Funcionario associado a esse usuário
        funcionario = Funcionario.objects.create(user=user)
        # Faz login com o usuário de teste
        self.client.login(username='testuser', password='testpassword')
        # Acessa a página inicial
        response = self.client.get(reverse('home'))
        # Verifica se a resposta usa o modelo 'main/home.html'
        self.assertTemplateUsed(response, 'main/home.html')

class SettingsViewTest(TestCase):
    def test_settings_view_status_code(self):
        # Cria um usuário de teste
        user = User.objects.create_user(username='testuser', password='testpassword')
        # Cria um objeto Funcionario associado a esse usuário
        funcionario = Funcionario.objects.create(user=user)
        # Faz login com o usuário de teste
        self.client.login(username='testuser', password='testpassword')
        # Acessa a página de configurações
        response = self.client.get(reverse('settings'))
        # Verifica se a resposta retorna um código de status HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_settings_view_template(self):
        # Cria um usuário de teste
        user = User.objects.create_user(username='testuser', password='testpassword')
        # Cria um objeto Funcionario associado a esse usuário
        funcionario = Funcionario.objects.create(user=user)
        # Faz login com o usuário de teste
        self.client.login(username='testuser', password='testpassword')
        # Acessa a página de configurações
        response = self.client.get(reverse('settings'))
        # Verifica se a resposta usa o modelo 'main/settings.html'
        self.assertTemplateUsed(response, 'main/settings.html')

class InscricaoViewTest(TestCase):
    def test_inscricao_view_redirect(self):
        # Cria um usuário de teste
        user = User.objects.create_user(username='testuser', password='testpassword')
        # Cria um objeto Funcionario associado a esse usuário
        funcionario = Funcionario.objects.create(user=user)
        # Faz login com o usuário de teste
        self.client.login(username='testuser', password='testpassword')
        # Tenta acessar a visualização de inscrição
        response = self.client.get(reverse('inscrever'))
        # Verifica se a resposta redireciona corretamente para a página inicial
        self.assertRedirects(response, reverse('home'))

    def test_inscricao_view_with_post(self):
        # Cria um usuário de teste
        user = User.objects.create_user(username='testuser', password='testpassword')
        # Cria um objeto Funcionario associado a esse usuário
        funcionario = Funcionario.objects.create(user=user)
        # Faz login com o usuário de teste
        self.client.login(username='testuser', password='testpassword')
        # Cria uma carona de exemplo
        carona = Carona.objects.create(
            motorista=user.funcionario,
            origem='Origem',
            destino='Destino',
            vagas_disponiveis=3,
            horario='2023-11-02T12:00:00Z',
            valor=10.0
        )
        # Envia um POST para a visualização de inscrição com o ID da carona
        response = self.client.post(reverse('inscrever'), {'carona_id': carona.id})
        # Verifica se a inscrição redireciona corretamente de volta à página inicial
        self.assertRedirects(response, reverse('home'))
