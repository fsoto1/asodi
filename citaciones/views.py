from django.shortcuts import render

# Create your views here.

def citacion(request):
	if not request.user.is_authenticated:
		return redirect('sas:login')
	return render(request,'citaciones/citacion.html')