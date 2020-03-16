from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('details/', views.phone, name='phone')
]
