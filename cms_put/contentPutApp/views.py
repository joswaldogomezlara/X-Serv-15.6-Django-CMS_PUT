from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home(request, page_name):

    if request.method == 'GET':

        try:
            page = Pages.objects.get(name=page_name)
            respuesta = page.body
        except Pages.DoesNotExist:
            respuesta = 'No existe esa pagina'

        return HttpResponse(respuesta)

    else:

        page = Pages(name=page_name, body=request.body)
        page.save()

        return HttpResponse('Pagina ' + page_name + ' creada correctamente')
