from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
	url(r'^entrar/$', views.LoginView.as_view(), name='login'),
	url(r'^salir/$', views.logout_view, name='logout'),
]