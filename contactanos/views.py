from django.shortcuts import render


# Create your views here.
def contactos(request):
    return render(request, "contactos.html")
