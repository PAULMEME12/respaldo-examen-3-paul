from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm

def lista_albumes(request):
    albumes = Album.objects.all()
    return render(request, 'albumes/lista_albumes.html', {'albumes': albumes})

def detalle_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albumes/detalle_album.html', {'album': album})

def nuevo_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_albumes')
    else:
        form = AlbumForm()
    return render(request, 'albumes/editar_album.html', {'form': form})

def editar_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('lista_albumes')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albumes/editar_album.html', {'form': form})

def eliminar_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('lista_albumes')