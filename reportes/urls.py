from django.conf.urls import url
from . import views

app_name = 'reportes' 

urlpatterns = [
	url(r'^todos/$', views.reportes, name='reportes'),
	url(r'^comunas/$', views.comunas, name='comunas'),
]