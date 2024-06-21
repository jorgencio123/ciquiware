from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'gestionusuario/index.html')


@login_required
def profile(request):
    return render(request, 'gestionusuario/profile.html')

@login_required
def grupo(request):
    return render(request, 'gestionusuario/grupo.html')


@login_required
def crearart(request):
    return render(request, 'gestionusuario/crearart.html')


@login_required
def crearart2(request):
    return render(request, 'gestionusuario/crearart2.html')

@login_required
def crearart3(request):
    return render(request, 'gestionusuario/crearart3.html')

@login_required
def crearart4(request):
    return render(request, 'gestionusuario/crearart4.html')

@login_required
def crearart5(request):
    return render(request, 'gestionusuario/crearart5.html')