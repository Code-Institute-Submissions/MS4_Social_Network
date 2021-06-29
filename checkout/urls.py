from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>/', views.checkout, name='checkout')
]
