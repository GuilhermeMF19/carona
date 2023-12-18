from django.shortcuts import render, redirect
from .forms import RegisterForm
from main.models import Funcionario 

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Crie um objeto Funcionario associado ao usuário recém-criado e inserir telefone
            funcionario, created = Funcionario.objects.get_or_create(user=user, telefone=form.cleaned_data['telefone'])
            
            return redirect("/")
    else:
        form = RegisterForm()
    
    return render(request, "register/register.html", {"form": form})
