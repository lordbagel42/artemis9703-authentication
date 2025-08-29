from django.urls import path
from .views import image_login_view
from .views import signup_view
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
#    path("", views.login, name="login"),
    path('', views.index, name='index'),
    path('login/', image_login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
