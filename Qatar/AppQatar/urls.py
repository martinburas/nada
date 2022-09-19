from django.urls import path

from AppQatar import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('seleccion', views.seleccion, name="Seleccion"),
    path('estadio', views.estadio, name="Estadio"),
    path('copas', views.copas, name="Copas"),
    path('buscar/', views.buscar),
   
]
