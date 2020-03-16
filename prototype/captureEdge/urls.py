from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sms/', views.user_details, name='user_details')
]
