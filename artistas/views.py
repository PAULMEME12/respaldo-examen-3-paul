from django.shortcuts import render, get_object_or_404, redirect
from .models import Artista
from .forms import ArtistaForm

def lista_artistas(request):
    artistas = Artista.objects.all()
    return render(request, 'artistas/lista_artistas.html', {'artistas': artistas})

def detalle_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    return render(request, 'artistas/detalle_artista.html', {'artista': artista})

def nuevo_artista(request):
    if request.method == "POST":
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_artistas')
    else:
        form = ArtistaForm()
    return render(request, 'artistas/editar_artista.html', {'form': form})

def editar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == "POST":
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('lista_artistas')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'artistas/editar_artista.html', {'form': form})

def eliminar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    artista.delete()
    return redirect('lista_artistas')