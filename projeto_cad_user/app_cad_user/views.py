from django.shortcuts import render
from .models import Usuario

# Create your views here.

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    
    # salvar os dados da tela para o banco
    
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('Nome')
    novo_usuario.idade = request.POST.get('Idade')
    novo_usuario.save()
