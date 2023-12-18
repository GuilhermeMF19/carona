from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inscrever', views.inscrever, name='inscrever'),
    path('settings/', views.settings, name='settings'),
    path('desistir', views.desistir, name='desistir'),
    path('cadastrar_carona/', views.cadastrar_carona, name='cadastrar_carona'),
    path('cadastrar_veiculo/', views.cadastrar_veiculo, name='cadastrar_veiculo'),
    path('excluir_carona/<int:carona_id>/', views.excluir_carona, name='excluir_carona'),
    path('concluir_carona/<int:carona_id>/', views.concluir_carona, name='concluir_carona'),
    path('excluir_veiculo/<int:veiculo_id>/', views.excluir_veiculo, name='excluir_veiculo'),
    path('aceitar_inscricao/<int:carona_id>/<int:inscricao_id>/', views.aceitar_inscricao, name='aceitar_inscricao'),
    path('rejeitar_inscricao/<int:carona_id>/<int:inscricao_id>/', views.rejeitar_inscricao, name='rejeitar_inscricao'),
    path('edit_carona/<int:carona_id>/', views.edit_carona, name='edit_carona'),
]