from django.conf.urls import url
from . import views

app_name = 'socios' 

urlpatterns = [
	url(r'^buscar/$', views.socio_list, name='buscar-socios'),
	url(r'^(?P<id>[0-9]+)/detalle$', views.socio_detail, name='socio'),
	url(r'^ingresar$', views.socio_add, name='agregar-socio'),
	url(r'^(?P<id>[0-9]+)/editar/$', views.socio_edit, name='editar-socio'),
	url(r'^(?P<id>[0-9]+)/eliminar/$', views.socio_delete, name='eliminar-socio'),
]