from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name = "welcome"),
    path('login', views.login, name = "login"),
    path('register', views.register, name = "register"),
    path('userprofile', views.userprofile, name = "userprofile"),
    path('user_logout', views.user_logout, name = "user_logout"),
    
]