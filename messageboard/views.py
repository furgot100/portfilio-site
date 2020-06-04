from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    message = "Message Board"
    return render(request, 'messageboard/home.html', {
        'message': message,
    })
