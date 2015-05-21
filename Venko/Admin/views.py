from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response
from models import *
from forms import *
from django.template.context import RequestContext
import datetime as hoy
import json
from django.core import serializers
# Create your views here.

def login(request):
	now = hoy.datetime.now()
	return render_to_response('login.html', {'hora': now})

#------------------------------Alumnos--------------------------------	
def alumnos(request):
	alumnos = Alumno.objects.all()
	for al in alumnos:
		al.pago=pagoMes(al)
		al.save()
	return render_to_response('alumnos.html',locals())

def borrar(request, id):
	alumno = Alumno.objects.get(pk=id)
	alumno.delete()
	return HttpResponseRedirect("/alumnos")

def pagoMes(a):
	d = hoy.date.today()
	pagos= Caja.objects.filter(alumno=a)
	for p in pagos:
		if p.fecha.month==7 and p.fecha.year==d.year:
			return True
	return False		
#------------------------------Alumnos--------------------------------	

def home(request):
	now = datetime.now()
	return render_to_response('index.html', {'hora': now})


def alumnosDetalle(request, id):
	alumno=  Alumno.objects.get(pk=id)
	if request.method == "POST":
		formA  = AlumnoCompletoForm(request.POST, instance=alumno)
		if formA.is_valid():
			formA.save()
			return HttpResponseRedirect("/alumnosDetalle/"+id)
		else:
			formD= DiagnosticoForm(request.POST)
			if formD.is_valid():
				formD.save()
			else:
				formAnte = AntecendenteForm(request.POST)	
				if formAnte.is_valid():
					formAnte.save()
	formALumno = AlumnoCompletoForm(instance=alumno)
	formDiags= DiagnosticoForm(initial={'alumno': alumno})
	formAntece = AntecendenteForm(initial={'alumno': alumno})
	diagnostico= Diagnostico.objects.filter(alumno=alumno)
	antecedentes= Antecedente.objects.filter(alumno=alumno)
	return render_to_response('alumnosDetalle.html', context_instance = RequestContext(request, locals()))	

def add(request):
	if request.method == "POST":
		form = AlumnoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/alumnos")
	else:
		form = AlumnoForm()
	template = "alumnonuevo.html"
	return render_to_response(template, context_instance = RequestContext(request, locals()))

#-------------------------- SERVICIOS------------------------------------------------------
	
def modServicio(request, id):
	s= Servicio.objects.get(pk=id)
	if request.method == "POST":
		formS  = ServicioForm(request.POST, instance=s)
		if formS.is_valid():
			formS.save()
			return HttpResponseRedirect("/servicios")
	f = ServicioForm(instance=s)
	template="modServicio.html"
	return render_to_response(template,  context_instance = RequestContext(request, locals()))

def servicios(request):
	servicios= Servicio.objects.all()
	template="servicios.html"
	return render_to_response(template, locals())


def addServicio(request):
	if request.method == "POST":
		form = ServicioForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/servicios")
	else:
		form = ServicioForm()
	template = "servicioNuevo.html"
	return render_to_response(template, context_instance = RequestContext(request, locals()))	

#--------------------PAGOS------------------------------------

def pagos(request):

	deudores=getDeudas()
	pagos= getHistorial()
	form = CajaIE()
	template="pagos.html"	
	if request.method == "POST":
		form = CajaIE(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/pagos")
		else:
			form2 = CajaIE(request.POST)
			if form2is_valid():
				return HttpResponseRedirect("/pagos")

	balance= Getbalance(hoy.date.today(),hoy.date.today())
	formC = CuentaForm()
	CantOperaciones= balance.count()
	#---------------------montos-------------------
	egreso=0
	ingreso=0
	alumno=0
	total=0
	for b in balance:
		if b.pago<0:	
			egreso += b.pago
		else:	
			if b.alumno:
				alumno+=b.pago
			else:
				ingreso +=b.pago
	total+=egreso+ingreso+alumno
	#----------------------montos-----------------------			
	return render_to_response(template,  context_instance = RequestContext(request, locals()))

def pagoDetalle(request, id):
	deudores=getDeudas()	
	pagos= getHistorial()	
	a= Alumno.objects.get(pk=id)
	s= Servicio.objects.get(pk=a.servicio.id)
	form = CajaForm(initial={'alumno': a,'pago':s.valor})
	template="pagos.html"
	return render_to_response(template,  context_instance = RequestContext(request, locals()))

def getDeudas():
	l=[]
	alumnos = Alumno.objects.all()
	for al in alumnos:
		if al.pago==False:
			ultPago=getPagos(al)
			if (ultPago):
				l.append((al,ultPago[0]))
	return l	

def getHistorial():
	pagos = Caja.objects.order_by("-fecha")
	return pagos	

def getPagos(al):
	pagos = Caja.objects.filter(alumno=al).order_by("-fecha")
	return pagos

def Getbalance(fechaI,fechaF):
	balance = Caja.objects.filter(fecha=fechaI).filter(fecha=fechaF)
	return balance


#-------------------- Json Methods-----------------------------
def getAlumnos(request):
	alumnos = Alumno.objects.all()
	data= serializers.serialize("json",alumnos)
	return HttpResponse(data, content_type='application/json')

	