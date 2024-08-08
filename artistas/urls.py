from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_artistas, name='lista_artistas'),
    path('<int:pk>/', views.detalle_artista, name='detalle_artista'),
    path('nuevo/', views.nuevo_artista, name='nuevo_artista'),
    path('<int:pk>/editar/', views.editar_artista, name='editar_artista'),
    path('<int:pk>/eliminar/', views.eliminar_artista, name='eliminar_artista'),
]