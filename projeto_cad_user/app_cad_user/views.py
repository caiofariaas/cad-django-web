from django.shortcuts import get_object_or_404, redirect, render
from .models import Usuario

# Create your views here.

def home(request):
    return render(request, 'usuarios/home.html')

def listar_usuarios(request):
    
    usuarios = Usuario.objects.all()
    
    return render(request, 'usuarios./usuarios.html',  {'usuarios': usuarios})

def usuarios(request):
    
    # salvar os dados da tela para o banco de dados
    
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('Nome')
    novo_usuario.idade = request.POST.get('Idade')
    novo_usuario.save()
    
    return redirect('/usuarios')


def excluir(request, id_user):
    
    usuario = get_object_or_404(Usuario, id_usuario = id_user)
    
    usuario.delete()
    
    return redirect('/usuarios')
    

def editar(request, id_user):
    usuario = get_object_or_404(Usuario, id_usuario=id_user)

    context = {'usuario': usuario} 
    return render(request, 'usuarios/edit_user.html', context)  


def editar_user(request, id_user):
    
    usuario = get_object_or_404(Usuario, id_usuario=id_user)
    
    if request.method == 'POST':

        dados = request.POST
        
        for campo, valor in dados.items():
            
            if campo in ["id"]:
                
                continue
            setattr(usuario, campo, valor)
            
        usuario.save()
        
        return redirect('/usuarios')
    