from django.urls import path
from app_cad_user import views

urlpatterns = [
    #rota, view responsável, nome de referencia
    #usuario.com
    
    path('', views.home, name='home'),
    
    #usuario.com/usuarios
    
    path('usuarios/', views.usuarios, name='listagem_usuarios')
    
    
    
]
