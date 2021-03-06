"""django_unchained URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from resume import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inner_page/', views.inner_page, name='inner_page'),
    path('admin/', admin.site.urls),
    path('contact_me/', views.contact_me, name='contact_me'),
    path('accounts/login/', views.my_login, name='login'),
    path('accounts/', include('registration.backends.simple.urls')),
]
