from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm
from django.contrib.auth.decorators import login_required

def lista_animales(request):
    animales = Animal.objects.all()
    return render(request, 'animales/lista_animales.html', {'animales': animales})

def agregar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_animales')
    else:
        form = AnimalForm()
    return render(request, 'animales/agregar_animal.html', {'form': form})

@login_required
def agregar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_animales')
    else:
        form = AnimalForm()
    return render(request, 'animales/agregar_animal.html', {'form': form})