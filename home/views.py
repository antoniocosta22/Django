from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def conteudo(request):
    return render(request, 'home/conteudo.html')

def login(request):
    return render(request, 'home/login.html')

def cadastro(request):
    return render(request, 'home/cadastro.html')

def auditoria(request):
    return render(request, 'home/auditoria.html')