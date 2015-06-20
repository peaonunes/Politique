from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Evento, CapacitacaoInterna, CapacitacaoExterna, EventoInstitucional
from Website.forms import CapacitacaoInternaForm
from Website.forms import CapacitacaoExternaForm
from Website.forms import EventoInstitucionalForm
from Website.forms import EventoForm

def EventoView(request):
    query = Evento.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)

def CadastrarEventoView(request):

	if request.method == 'POST':

		auxForm = EventoForm(request.POST)
		
		if auxForm.is_valid():

			tipo = auxForm.cleaned_data['tipoEvento']

			if tipo == "1":

				form = CapacitacaoInternaForm(request.POST or None)

			elif tipo == "2":

				form = CapacitacaoExternaForm(request.POST or None)

			elif tipo == "3":

				form = EventoInstitucionalForm(request.POST or None)

			else:

				form = Evento(request.POST or None)

			if form.is_valid():
				form.save()

		else:
			form = Evento(None)

	else:
		form = Evento(None)
		
	return render(request, 'cadastrarEvento.html', {"form":form})

def ConsultarEventoView(request):
	eventos = Evento.objects.filter().order_by('nome')
	capacitacoesInternas = CapacitacaoInterna.objects.filter().order_by('nome')
	capacitacoesExternas = CapacitacaoExterna.objects.filter().order_by('nome')
	eventosInstitucionais = EventoInstitucional.objects.filter().order_by('nome')
	return render(request, 'consultarEvento.html', {'eventos': eventos, 'capacitacoesInternas': capacitacoesInternas, 'capacitacoesExternas': capacitacoesExternas, 'eventosInstitucionais': eventosInstitucionais})

def RemoverEventoView(request, id):
    obj = Evento.objects.get(pk=id)
    obj.delete()
    return render(request, 'consultarEvento.html')




