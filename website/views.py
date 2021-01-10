
from django.shortcuts import render

def hello_blog(request):
    lista = ["django", "python", "html5","git"]
    data = {"name": "curso de django3", "lista_tecnologia":lista}
    return render(request, "index.html", data)