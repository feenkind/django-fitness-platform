from django.shortcuts import render
#from django.http import HttpResponse

def base_view(request, *args, **kwargs):
    context = {}
    return render(request, 'base.html', context)

def start_view(request, *args, **kwargs):
    context = {
        "page_title": "Startseite"
    }
    return render (request, "startpage.html", context)


def fitnessplans_view(request, *args, **kwargs):
    context = {
        "page_title": "Fitnesspläne"
    }
    return render(request, 'fitnessplans.html', context)

def food_view(request, *args, **kwargs):
    context = {
        "page_title": "Gesunde Ernährung"
    }
    return render(request, 'healthyfood.html', context)
