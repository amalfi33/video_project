
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('videos/', views.videos, name = 'videos'),
    path('videos/<slug:slug>', views.post_detail, name = 'post_detail_url'),
]
