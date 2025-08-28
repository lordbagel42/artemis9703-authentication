from django.urls import path
from .views import image_login_view
from .views import signup_view
from . import views

urlpatterns = [
#    path("", views.login, name="login"),
    path('', image_login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]