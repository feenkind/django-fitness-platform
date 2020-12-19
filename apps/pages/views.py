from django.shortcuts import render
from django.http import HttpResponse

def start_page(request):
    return render(request, 'base.html', {'page_title': 'Here will be the awesome start page!',})
