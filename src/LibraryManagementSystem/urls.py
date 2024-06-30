"""
URL configuration for LibraryManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('createBook/', views.createBook, name='createBook'),
    path('updateBook/<str:pk>/', views.updateBook, name='updateBook'),
    path('deleteBook/<str:pk>/', views.deleteBook, name='deleteBook'),
    path('borrowList/', views.borrowList, name='borrowList'),
    path('borrowBook/', views.borrowBook, name='borrowBook'),
    path('returnBook/<str:pk>/', views.returnBook, name='returnBook'),
    path('userBorrowed/', views.userBorrowed, name='userBorrowed'),


]
