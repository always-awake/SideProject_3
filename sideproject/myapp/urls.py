from django.urls import path
from . import views

urlpatterns = [
    path('', views.myview),
    path('redirect/', views.myview2),
]
