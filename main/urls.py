"""octa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chatterbox/', chatterbox, name='chatterbox'),
    url(r'^dbapi/', dbapi, name='dbapi'),
    url(r'^rand/', rand, name='random'),
    url(r'^statistics/messages', get_user_message_statistics, name='get_user_message_statistics'),
    url(r'^statistics/cities_searched_present', get_cities_searched_present_statistics, name='statistics/cities_searched_present'),
    url(r'^statistics/cities_searched_absent', get_cities_searched_absent_statistics, name='statistics/cities_searched_absent'),
    url(r'^statistics/countries', get_countries_statistics, name='statistics/countries'),
    url(r'^statistics/users', get_user_statistics, name='statistics/users'),
]
