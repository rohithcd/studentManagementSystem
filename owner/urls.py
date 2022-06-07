# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('approve', views.approve,name='approve'),
    path('reject/<userid>',views.reject,name='reject'),
    path('select/<userid>',views.select,name='select')

]