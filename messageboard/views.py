from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    message = "Welcome to the message board"
    return render(request, 'messageboard/home.html', {
        'message': message,
    })
