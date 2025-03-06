
from django.contrib import admin
from django.urls import path
from hospitalapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index,name='home'),
    path('service/', views.service,name='service'),

    path('starter/', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('departments/', views.departments,name='departments'),
    path('doctors/', views.doctors,name='doctors'),
    path('appointment/', views.Appoint,name='appointment'),
    path('contact/', views.contacts,name='contact'),
    path('show/', views.show,name='show'),
    path('delete/<int:id>', views.delete, ),
    path('edit/<int:id>', views.edit, name='edit'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),


]
