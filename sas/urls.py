from django.conf.urls import url
from . import views
from login.views import LoginView, logout_view
from socios.views import buscar_socios

app_name = 'sas' 

urlpatterns = [
	#home
	url(r'^$', views.index, name='index'),
	#login
	url(r'^login/$', LoginView.as_view(), name='login'),
	url(r'^logout/$', logout_view, name='logout'),
	#socios
	url(r'^buscar-socios/$', buscar_socios, name='buscar-socios'),
]