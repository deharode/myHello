#importar modulos
from django.http import HttpResponse
import datetime


#definir una funcion que cree una pagina web
def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>Hello World, the time: %s </body></html>" %now
    return HttpResponse(html)
