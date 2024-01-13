"""
URL configuration for Redbus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home import views as home_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_views.home,name='home'),
    path('accounts/signup',accounts_views.signup,name='signup'),
    path('accounts/login',accounts_views.login,name='login'),
    path('accounts/logout',accounts_views.logout,name='logout'),
    path('journey',home_views.journey,name='journey'),
    path('edit/<int:pk>',home_views.edit,name='edit'),
    path('confirm/<str:f>',home_views.confirm,name='confirm'),
    path('delete/<int:pk>',home_views.delete,name='delete'),
    path('tickets',home_views.tickets,name='tickets')
        
    
]
