from django.shortcuts import render
from django.http import HttpResponse

def start_page(request):
    return HttpResponse('<!DOCTYPE><html><body>Here will be the awesome start page!</body></html>')
