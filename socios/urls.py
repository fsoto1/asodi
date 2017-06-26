from django.conf.urls import url
from . import views

app_name = 'socios' 

urlpatterns = [
	url(r'^buscar/$', views.buscar, name='buscar-socios'),
	url(r'^socio/$', views.socio, name='socio'),
	url(r'^ingresar$', views.agregar_socio, name='agregar-socio'),
]