from django.urls import path

from . import views

urlpatterns = [
    path('language/', views.language),
    path('system/', views.system),
    path('ide/', views.ide),
    path('', views.nothing)
]