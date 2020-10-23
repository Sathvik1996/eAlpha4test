from django.urls import path
from . import views

urlpatterns = [
    path('', views.manager, name = "manager"),
    path('login', views.managerlogin, name = "managerlogin"),
    path('edit', views.edit, name = "edit"),
    path('edit/post',views.edit_post_request_method, name= 'edit_post_request_method'),
    path('create', views.create , name = "create"),
    path('manager_logout', views.manager_logout , name = "manager_logout"),
    
]