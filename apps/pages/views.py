from django.shortcuts import render

def start_view(request, *args, **kwargs):
    context = {
        'page_title': 'Startseite'
    }
    return render (request, 'pages/startpage.html', context)

