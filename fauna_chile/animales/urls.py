from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_animales, name='lista_animales'),
    path('agregar/', views.agregar_animal, name='agregar_animal'),
]