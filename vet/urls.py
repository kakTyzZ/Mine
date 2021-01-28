"""vet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include


from main.views import (
    index_view,
    dogs_view,
    cats_view,
    rodents_view,
    fish_view,
    birds_view,
    reptiles_view,
    test_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
    path('', index_view, name='main'),
    path('dogs/', dogs_view, name='dogs'),
    path('cats/', cats_view, name='cats'),
    path('rodents/', rodents_view, name='rodents'),
    path('fish/', fish_view, name='fish'),
    path('birds/', birds_view, name='birds'),
    path('reptiles/', reptiles_view, name='reptiles'),
    path('test/', test_view, name='test'),
]
