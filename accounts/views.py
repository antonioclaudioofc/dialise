from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'login.html')
    
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    
    user = auth.authenticate(request, username=usuario, password=senha)
    
    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez o login com sucesso')
        return redirect('dashlog')

@login_required(redirect_field_name='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'cadastro.html')
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    
    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.add_message(request, messages.INFO, 'Nenhum campo pode ficar vazio')
        return render(request, 'cadastro.html')
    
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'cadastro.html')
    
    if len(senha) < 6:
        messages.error(request, 'Senha muito pequena')
        return render(request, 'cadastro.html')
    
    if senha != senha2:
        messages.error(request, 'Senhas não conferem')
        return render(request, 'cadastro.html')
    
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe')
        return render(request, 'cadastro.html')
    
    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe')
        return render(request, 'cadastro.html')
    
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    
    messages.success(request, 'Usuário cadastrado, faça login')
    return redirect('login')

@login_required(redirect_field_name='login')
def dashlog(request):
    return render(request, 'dashlog.html')