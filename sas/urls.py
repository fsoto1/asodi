from django.conf.urls import url
from . import views
from login.views import LoginView, logout_view
from socios.views import  buscar, socio

app_name = 'sas' 

urlpatterns = [
	#home
	url(r'^$', views.index, name='index'),
	#login
	url(r'^login/$', LoginView.as_view(), name='login'),
	url(r'^logout/$', logout_view, name='logout'),
	#socios
	url(r'^buscar-socios/$', buscar, name='buscar-socios'),
	url(r'^socio/$', socio, name='socio'),
]