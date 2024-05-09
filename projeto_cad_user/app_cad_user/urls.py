from django.urls import path
from . import views


urlpatterns = [ 
    
    path ('excluir/<int:id_user>', views.excluir, name = 'excluir'),
    
    path('editar/<int:id_user>', views.editar, name='editar_usuario'),
    path('editar_user/<int:id_user>', views.editar_user, name='editar_usuario_final'),

    path('usuarios', views.listar_usuarios, name='listar_usuarios'),
    
    path('cad_user', views.usuarios, name='cad_user')
    
]