
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from login.models import Users_db

from login.forms import Users_dbForm

# Create your views here.
def sesiones(request):
    if request.method == "POST":
        formaUser_db = Users_dbForm(request.POST)
        if formaUser_db.is_valid():
            usuario = request.POST['user']
            contraseña = request.POST["passw"]
            print(f'Usuario: {usuario}\nContraseña: {contraseña}')
            validacion_credenciales = verificarUsuario(usuario, contraseña)
            if validacion_credenciales:
                # Si credenciales validas redirecciona el usuario y su estado a otra página
                return HttpResponse(validacion_credenciales)
            else:
                # Falta agregar mensaje de error al login
                redirect("login.html")
    else:
        formaUser_db = Users_dbForm()
    return render(request, "login.html", {"formaUser_db": formaUser_db})

def verificarUsuario(usuario, contraseña):
    persona = Users_db.objects.all().filter(user=usuario, passw=contraseña).values("user","state")
    return persona