from django.urls import path
from . import views

urlpatterns = [
    path('star/', views.star, name='star'),
]