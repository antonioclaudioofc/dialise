from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from .models import Paciente
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(redirect_field_name='login')
def dashboard(request):
    messages.add_message(request, messages.SUCCESS, 'Bem-vindo')
    return render(request, 'dashboard.html')

@login_required(redirect_field_name='login')
def painel(request):
    pacientes = Paciente.objects.order_by('-id').filter(
        mostrar=True #substitui o if 
        ) #.orderby('nome') > vai ordenar de A a Z se colocar (-nome) ordenar de Z a A, pode ordenar usando os dados da tabela do BD
    paginator = Paginator(pacientes, 5)
    
    page = request.GET.get("p")
    pacientes = paginator.get_page(page)
    
    return render(request, 'painel.html', {'pacientes': pacientes} )

@login_required(redirect_field_name='login')
def ver_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    
    if not paciente.mostrar:
        raise Http404()
    
    return render(request, 'ver_paciente.html', {'paciente': paciente, 'paciente_id': paciente.id})

@login_required(redirect_field_name='login')
def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')
    
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, "O campo não pode ficar vazio")
        return redirect('painel')
    
    pacientes = Paciente.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(contato__icontains=termo)
    )
    #pacientes = Paciente.objects.order_by('-id').filter(
    #    Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
    #    mostrar=True #substitui o if 
    #    ) #.orderby('nome') > vai ordenar de A a Z se colocar (-nome) ordenar de Z a A, pode ordenar usando os dados da tabela do BD
    paginator = Paginator(pacientes, 5)
    
    page = request.GET.get("p")
    pacientes = paginator.get_page(page)
    
    return render(request, 'busca.html', {'pacientes': pacientes} )
