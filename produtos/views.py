from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.

def ver_produto(request): 
    if request.method == 'GET':
        nome = 'vinicius'   
        #return render(request, 'ver_produto.html', {'nome': 'vinicius'})
        return HttpResponse('Deu certo o GET')
    elif request.method == 'POST': 
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        print(nome)
        print(idade)
        return HttpResponse(f"Deu certo o POST <br /> Nome: {request.POST.get('nome')}<br /> Idade: {request.POST.get('idade')}")
        







def inserir_produto(request):
    return render(request, 'inserir_produto.html')






