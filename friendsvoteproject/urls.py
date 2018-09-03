"""friendsvoteproject URL Configuration

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
from django.conf.urls import include, url
# from django.contrib import admin
from friendsvoteapp import views as friends_vote_views
from friendsvoteapp import urls as friends_vote_urls

urlpatterns = [
  url(r'^$', friends_vote_views.home_page, name='home'),
  url(r'^friendsvote/', include(friends_vote_urls), name='home'),
  # url(r'^admin/', admin.site.urls),
]
