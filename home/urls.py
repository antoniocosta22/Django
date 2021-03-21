from django.urls import path
from . import views


#clientes
urlpatterns = [
    path('', views.index),
    path('conteudo/', views.conteudo),
    path('login/', views.login),
]