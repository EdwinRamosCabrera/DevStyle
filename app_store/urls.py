from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app_store'

urlpatterns = [
    path('', views.StoreView.as_view(), name='store'),
]