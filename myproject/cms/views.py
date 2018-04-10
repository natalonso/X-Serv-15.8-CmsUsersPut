from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .models import Page

formulario = """
<form action="" method="POST">
    Name: <input type="text" name="name"><br>
    Page: <input type="text" name="page"><br>
    <input type="submit" value="Enviar">
</form>

"""
@csrf_exempt
def home(request): #PAGINA PRINCIPAL

    if request.method == 'POST':
        newpage= Page(name=request.POST['name'], page=request.POST['page'])
        newpage.save()

    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username
        permiso = True
    else:
        logged = 'Not logged in.'
        permiso = False

    lista = Page.objects.all()
    salida = "Bienvenido al servidor CMS, estas son las paginas disponibles hasta el momento: "
    salida += "<ul>"
    for pagina in lista:
        salida += '<li><a href=' + str(pagina.name) + '>' + pagina.name + '</a>'
    salida += "</ul>"


    if permiso == True: #estas logeado
        return HttpResponse(logged + '<br><a href= "/logout">Logout</a><br><br>' + salida + formulario )
    else: #no estas logeado
        return HttpResponse(logged + '<br><a href= "/login">Login</a><br><br>' + salida)

@csrf_exempt
def pagina(request, pagina):

    lista = Page.objects.all()
    for elemento in lista:
        if elemento.name == pagina:
            salida = elemento.page
            break
        else:
            salida = None
    if salida == None:
        return HttpResponse('Lo sentimos. La pagina no esta en la base de datos por el momento.')
    else:
        return HttpResponse(salida)
