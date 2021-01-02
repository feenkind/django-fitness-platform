from django.shortcuts import render
#from django.http import HttpResponse

def start_view(request, *args, **kwargs):
    context = {
        "page_title": "Startseite"
    }
    return render (request, "pages/startpage.html", context)


def fitnessplans_view(request, *args, **kwargs):
    context = {
        "page_title": "Fitnesspläne"
    }
    return render(request, 'pages/fitnessplans.html', context)

def food_view(request, *args, **kwargs):
    context = {
        "page_title": "Gesunde Ernährung"
    }
    return render(request, 'pages/healthyfood.html', context)
