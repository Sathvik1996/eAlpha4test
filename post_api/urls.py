from django.urls import path
from . import views

urlpatterns = [
    path('user_data/<str:username>/', views.main_api.as_view(), name='main_api'),
    
    
]