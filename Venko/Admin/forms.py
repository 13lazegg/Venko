from django import forms
from django.forms import ModelForm
from models import *
from django.utils.translation import ugettext_lazy as _


class AlumnoForm(ModelForm):
	class Meta:
		model = Alumno
		labels  = {
			'nombre': _('Nombre'),
			'fechanacimiento': _('Fecha de nacimiento'),
			'direccion': _('Direccion'),
		}
		exclude = ["obrasocial","profesion","deporte","medicotratante","derivadopor","medicacion","peso","talla","descuento","pago"]
	
class AlumnoCompletoForm(ModelForm):
	class Meta:
		model = Alumno
		labels  = {
			'nombre': _('Nombre'),
			'fechanacimiento': _('Fecha de nacimiento'),
			'direccion': _('Direccion'),
			'medicotratante': _('Medico tratante'),
			'derivadopor': _('Derivado por'),
			'obrasocial': _('Obra social'),
		}
		widgets = {'alumno': forms.HiddenInput()}

class DiagnosticoForm(ModelForm):
	class Meta:
		model = Diagnostico
		labels  = {
			'estadoactual': _('Estado actual'),
			'tiempoevolucion': _('Tiempo de evolucion'),
			'tratamientoactual': _('Tratamiento actual'),
			'mecanismoaccion': _('Mecanismo de accion'),
			'estudioscomplementarios': _('Estudios complementarios'),
			'antecedentesconsideracion': _('Antecedentes de consideracion'),
			
		}
		widgets = {'alumno': forms.HiddenInput()}
class AntecendenteForm(ModelForm):
	class Meta:
		model = Antecedente
		widgets = {'alumno': forms.HiddenInput()}

class ServicioForm(ModelForm):
	class Meta:
		model=Servicio	 

class PagoForm(ModelForm):
	class Meta:
		model=PagoCuenta	 		