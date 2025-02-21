
from django.contrib import admin
from django.urls import path
from hospitalapp import views
from hospitalapp.views import service

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('service/', views.service,name='service'),
    path('starter/', views.starter,name='starter'),

]
