from django.conf.urls import url
from . import views

app_name = 'socios' 

urlpatterns = [
	#socios
	url(r'^buscar/$', views.socio_list, name='buscar-socios'),
	url(r'^(?P<id>[0-9]+)/detalle$', views.socio_detail, name='socio'),
	url(r'^ingresar$', views.socio_add, name='agregar-socio'),
	url(r'^(?P<id>[0-9]+)/editar/$', views.socio_edit, name='editar-socio'),
	url(r'^(?P<id>[0-9]+)/eliminar/$', views.socio_delete, name='eliminar-socio'),
	#apoderado
	url(r'^apoderados/buscar/$', views.apoderado_list, name='buscar-apoderado'),
	url(r'^apoderados/(?P<id>[0-9]+)/detalle$', views.apoderado_detail, name='apoderado'),
	url(r'^apoderados/ingresar$', views.apoderado_add, name='agregar-apoderado'),
	url(r'^apoderados/(?P<id>[0-9]+)/editar/$', views.apoderado_edit, name='editar-apoderado'),
	url(r'^apoderados/(?P<id>[0-9]+)/eliminar/$', views.apoderado_delete, name='eliminar-apoderado'),

	url(r'^export/socios/xls/$', views.export_socios, name='export_socios'),
	url(r'^export/apoderados/xls/$', views.export_apoderados, name='export_apoderados'),
]