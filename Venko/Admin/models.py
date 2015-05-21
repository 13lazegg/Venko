from django.db import models
import datetime
# Create your models here.

class Servicio(models.Model):
	tipoServicio= models.CharField(max_length = 40)
	vecesPorSemana= models.IntegerField(max_length = 1)
	valor = models.IntegerField(max_length = 4)

	def __unicode__(self):
		return self.tipoServicio

class Alumno(models.Model):

	fechaingreso = models.DateTimeField(auto_now_add=True, blank=True)
	nombre = models.CharField(max_length = 80, blank=True)
	fechanacimiento = models.DateField(blank=True)
	direccion = models.CharField(max_length = 50, blank=True)
	telefono = models.CharField(max_length = 17, blank=True)
	email = models.CharField(max_length = 35, blank=True)
	obrasocial = models.CharField(max_length = 40, blank=True)
	profesion = models.CharField(max_length = 50, blank=True)
	deporte = models.CharField(max_length = 25, blank=True)
	medicotratante = models.CharField(max_length = 25, blank=True)
	derivadopor = models.CharField(max_length = 25, blank=True)
	medicacion = models.CharField(max_length = 140, blank=True)
	peso = models.IntegerField(max_length = 10, null=True, blank=True)
	talla = models.IntegerField(max_length = 10,null=True, blank=True)
	servicio = models.ForeignKey(Servicio)
	descuento = models.IntegerField(max_length = 4, default=0, blank=True)
	pago = models.BooleanField(default=False, blank=True,)
	def __unicode__(self):
		return self.nombre

class Diagnostico(models.Model):
	alumno = models.ForeignKey(Alumno)
	diagnostico = models.CharField(max_length = 250)
	estadoactual = models.CharField(max_length = 250)
	tiempoevolucion = models.CharField(max_length = 140)
	tratamientoactual = models.CharField(max_length = 140)
	anteriores = models.CharField(max_length = 140)
	mecanismoaccion = models.CharField(max_length = 140)
	estudioscomplementarios = models.CharField(max_length = 140)
	antecedentesconsideracion = models.CharField(max_length = 140)
	ta = models.IntegerField(max_length = 5)
	fc = models.CharField(max_length = 5)
	hta = models.CharField(max_length = 5)
	dbt = models.BooleanField(default=None)
	dislipemias = models.BooleanField(default=None)
	tabaco = models.BooleanField(default=None)
	arritmias = models.BooleanField(default=None)
	desmayos = models.BooleanField(default=None)
	tiroides = models.BooleanField(default=None)

	def __unicode__(self):
		return "%s - %i" % (self.alumno.nombre, self.id)

class Antecedente(models.Model):
	alumno = models.ForeignKey(Alumno)
	deporte = models.CharField(max_length = 15)
	frecuencia = models.CharField(max_length = 15)
	plantillas = models.BooleanField(default=None)
	dolores = models.CharField(max_length = 50)
	objetivos = models.CharField(max_length = 140)

	def __unicode__(self):
		return "%s - %i" % (self.alumno.nombre, self.id)

class PagoCuenta(models.Model):
	alumno = models.ForeignKey(Alumno)
	fecha = models.DateField(default=datetime.date.today())
	pago= models.IntegerField()


	def __unicode__(self):
		return (self.alumno.nombre,)