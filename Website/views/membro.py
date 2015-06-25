from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Setor, CustomUser
from Website.forms import CustomUserForm
from django.core import serializers
from django.contrib.auth.decorators import login_required

@login_required(login_url='/Website')
def cadastrarMembroView(request):

    user_form = CustomUserForm(request.POST or None)

    # CONFERIR SETOR E SETAR PERMISSOES DE ACORDO COM SETOR

    if user_form.is_valid():
        user_form.save()

    return render(request, 'cadastrarmembro.html', {"form": user_form})

@login_required(login_url='/Website')
def AtualizarMembroView(request, id):
    obj = CystomUser.objects.get(pk=id)
    return render(request, 'consultarMembro.html')

@login_required(login_url='/Website')
def ConsultarMembroView(request):
    membros = serializers.serialize( "python", CustomUser.objects.filter().order_by('username'), fields=('username','first_name', 'setor') )
    return render(request, 'consultarMembro.html', {'membros': membros})

@login_required(login_url='/Website')
def RemoverMembroView(request, id):
    obj = CystomUser.objects.get(pk=id)
    obj.is_active=False
    return render(request, 'consultarMembro.html')
