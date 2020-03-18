from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sms/', views.user_details, name='user_details'),
    path('upload/<int:claim_id>/<str:phone>/', views.upload_form, name='upload_form'),
 	# path('upload/', views.upload_images, name='upload_images')
]
