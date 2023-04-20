from django.shortcuts import render
from .models import HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def index(request):
     return HttpResponse('loja de cartas')

  
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        nome= request.POST.get('nome')
        nome= request.POST.get('senha')
        usuario = User.objects.filter(username=nome).first()
        if usuario:
            return HttpResponse('Usuario %s ja existe!' % (nome))
        return HttpResponse('Usuario: %s\nsenha: %s' %(nome, senha))
