from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('greet/<str:name>/', views.greet_by_name),
]