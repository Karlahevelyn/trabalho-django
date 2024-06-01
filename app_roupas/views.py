from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Roupas  # Supondo que você tenha um modelo chamado Roupas
from django.shortcuts import render
from .models import Roupa


def home(request):
    return render(request, 'roupas/home.html')

# Salva os dados no banco de dados


def roupas(request):
    nova_roupa = Roupa()
    nova_roupa.tipo = request.POST.get('tipo')
    nova_roupa.cor = request.POST.get('cor')
    nova_roupa.save()
    # Exibi os dados cadastrados
    roupas = {
        'roupas': Roupa.objects.all()
    }
    return render(request, 'roupas/roupas.html', roupas)


def inicio(request):
    return render(request, 'roupas/inicio.html')


def base(request):
    return render(request, 'roupas/base.html')


def login(request):
    return render(request, 'roupas/login.html')


def roupas(request):
    return render(request, 'roupas/roupas.html')


def femininas(request):
    return render(request, 'roupas/femininas.html')


def masculinas(request):
    return render(request, 'roupas/masculinas.html')


def pesquisar(request):
    query = request.GET.get('q')
    if query:
        # Ajuste o campo de acordo com o seu modelo
        resultados = Roupas.objects.filter(nome__icontains=query)
    else:
        resultados = Roupas.objects.all()
    return render(request, 'app_roupas/roupas.html', {'resultados': resultados, 'query': query})
