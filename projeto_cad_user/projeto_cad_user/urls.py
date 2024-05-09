from django.urls import include, path
from app_cad_user import views

urlpatterns = [
    #rota, view responsável, nome de referencia
    #usuario.com
    
    path('', views.home, name='home'),
    
    #usuario.com/usuarios

    path('', include('app_cad_user.urls'))
]
