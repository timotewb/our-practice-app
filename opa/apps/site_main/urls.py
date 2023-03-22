from django.urls import path
from . import views

app_name = "sm"
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_request, name='register'),
]