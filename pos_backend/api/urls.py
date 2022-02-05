from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('favorito',views.FavoritoView.as_view(),name='favorito')
]