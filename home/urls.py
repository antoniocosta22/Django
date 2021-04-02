from django.urls import path
from . import views


#clientes
urlpatterns = [
    path('', views.index),
    path('conteudo/', views.conteudo),
    path('login/', views.login),
    path('cadastro/', views.cadastro),
    path('auditoria/', views.auditoria),
]