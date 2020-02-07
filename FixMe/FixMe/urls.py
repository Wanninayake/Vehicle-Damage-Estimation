"""FixMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from pages.views import home_view, contact_view, signIn_view, signUp_view, imageUpload_view, estimation_view, temp_view, about_view

urlpatterns = [
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('signin/', signIn_view,name='signin'),
    path('signup/', signUp_view, name='signup'),
    path('about/', about_view, name='about'),
    path('imageupload/', imageUpload_view, name='imageupload'),
    path('estimation/', estimation_view, name='estimation'),
    path('temp/', temp_view, name='temp'),
    path('event/', temp_view, name='event'),
    path('admin/', admin.site.urls),
]
