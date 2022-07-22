from django.urls import path
from verify import views

urlpatterns = [
    path('', views.home),
    path('authenticate', views.authenticate)
]
