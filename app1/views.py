from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vistaUno(request):
    html="""
    <h1 style="color:green">Hola wenas</h1>    
"""

return HttpResponse(html)