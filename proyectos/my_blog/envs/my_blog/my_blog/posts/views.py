from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.
# Creamos la clase hola mundo para la vista 
class HolaMundoView(View):
    def get(self, request):
        return render(request, 'hello_world.html', context={})
