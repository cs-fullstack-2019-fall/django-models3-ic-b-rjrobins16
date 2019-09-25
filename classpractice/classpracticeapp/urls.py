from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addHouse/', views.newhouse, name='newhouse'),
    path('bed/', views.printBed),
    path('sqft/', views.squarefeetchanger),
]
