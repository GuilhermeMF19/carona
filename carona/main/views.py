from django.shortcuts import render, redirect
from .forms import CaronaForm, VeiculoForm, EditCaronaForm
from .models import Carona, Veiculo, Funcionario, InscricaoCarona

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    caronas = Carona.objects.all()
    inscricoes = InscricaoCarona.objects.all()
            
    return render(request, 'main/home.html', {'caronas': caronas, 'inscricoes': inscricoes})

@login_required
def inscrever(request):
    carona_id = None

    if request.method == 'POST':
        carona_id = request.POST.get('carona_id')
    if carona_id:
        carona = Carona.objects.get(id=carona_id)
        # Verifica se o usuário já se inscreveu
        inscricao_existente = InscricaoCarona.objects.filter(carona=carona, funcionario=request.user.funcionario).exists()
        if not inscricao_existente:
            inscricao = InscricaoCarona(carona=carona, funcionario=request.user.funcionario, status='P')
            inscricao.save()
    
    return redirect('home')

@login_required
def settings(request):
    user = request.user
    veiculos = Veiculo.objects.filter(funcionario__user=user)
    caronas = Carona.objects.filter(motorista__user=user)
    inscricoes = InscricaoCarona.objects.all()
    minhasinscricoes = InscricaoCarona.objects.filter(funcionario__user=user)
    
    funcionario = Funcionario.objects.get(user=user)
    if  funcionario.veiculos.exists():
        carona_form = CaronaForm(request.user.id)
    else:
        carona_form = None
        
    veiculo_form = VeiculoForm()
    edit_carona_form = EditCaronaForm()

    return render(request, 'main/settings.html', 
                  {'carona_form': carona_form, 
                   'veiculo_form': veiculo_form, 
                   'edit_carona_form': edit_carona_form, 
                   'caronas': caronas, 'veiculos': veiculos, 
                   'inscricoes': inscricoes, 
                   'minhasinscricoes': minhasinscricoes,})
    
@login_required
def desistir(request):
    carona_id = None

    if request.method == 'POST':
        carona_id = request.POST.get('carona_id')
        try:
            carona = Carona.objects.get(id=carona_id)
            inscricao = InscricaoCarona.objects.filter(carona=carona, funcionario=request.user.funcionario).first()
            if inscricao:
                inscricao.delete()
        except inscricao.DoesNotExist:
            pass        
    return redirect('settings')

@login_required
def cadastrar_carona(request):
    if request.method == 'POST':
        carona_form = CaronaForm(request.user.id, request.POST)
        if carona_form.is_valid():
            carona = carona_form.save(commit=False)
            carona.motorista = request.user.funcionario
            carona_form.save()
            return redirect('settings')

    return redirect('settings') 

@login_required
def cadastrar_veiculo(request):
    if request.method == 'POST':
        veiculo_form = VeiculoForm(request.POST)
        if veiculo_form.is_valid():
            veiculo = veiculo_form.save(commit=False)
            veiculo.funcionario = request.user.funcionario
            veiculo.save()
            return redirect('settings')

    return redirect('settings') 

@login_required
def excluir_carona(request, carona_id):
    try:
        carona = Carona.objects.get(id=carona_id)
        carona.delete()
    except Carona.DoesNotExist:
        pass 
    
    return redirect('settings')

@login_required
def concluir_carona(request, carona_id):
    try:
        carona = Carona.objects.get(id=carona_id)
        carona.vagas_disponiveis = 0
        carona.save()
    except Carona.DoesNotExist:
        pass 
    
    return redirect('settings')

@login_required
def excluir_veiculo(request, veiculo_id):
    try:
        veiculo = Veiculo.objects.get(id=veiculo_id)
        veiculo.delete()
    except Veiculo.DoesNotExist:
        pass 
    
    return redirect('settings')

@login_required
def aceitar_inscricao(request, carona_id, inscricao_id):

    carona = Carona.objects.get(id=carona_id)
    if request.user == carona.motorista.user:
        inscricao = InscricaoCarona.objects.get(id=inscricao_id)
        if inscricao.status == 'P':
            inscricao.status = 'A'  
            inscricao.save()
            carona.vagas_disponiveis -= 1  
            carona.save()
    
    return redirect('settings')

@login_required
def rejeitar_inscricao(request, carona_id, inscricao_id):

    carona = Carona.objects.get(id=carona_id)
    if request.user == carona.motorista.user:
        inscricao = InscricaoCarona.objects.get(id=inscricao_id)
        if inscricao.status == 'P':
            inscricao.status = 'R'  
            inscricao.save()
            carona.save()
    
    return redirect('settings')

@login_required
def edit_carona(request, carona_id):
    carona = Carona.objects.get(id=carona_id)

    if request.method == 'POST':
        form = EditCaronaForm(request.POST, instance=carona)
        if form.is_valid():
            if form.cleaned_data['valor'] is None:
               
                form.cleaned_data['valor'] = carona.valor

         
            carona = form.save()
            return redirect('settings')

    else:
        form = EditCaronaForm(instance=carona)

    return redirect('settings')
        
    





