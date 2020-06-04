from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    home = "Portfolio Homepage"
    return render(request, 'portfolio/home.html', {
        'home' : home,
    })

def contact(request):
    contact = "Contact Me"
    return render(request, 'portfolio/contact.html',{
        'contact' : contact,
    })

def greet_by_name(request, name):
    message = "Hello, %s!" % name
    return render(request, 'portfolio/greet.html', {
        'message' : message,
    })

