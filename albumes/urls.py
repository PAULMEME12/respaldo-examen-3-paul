from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_albumes, name='lista_albumes'),
    path('<int:pk>/', views.detalle_album, name='detalle_album'),
    path('nuevo/', views.nuevo_album, name='nuevo_album'),
    path('<int:pk>/editar/', views.editar_album, name='editar_album'),
    path('<int:pk>/eliminar/', views.eliminar_album, name='eliminar_album'),
]