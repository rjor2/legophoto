__author__ = 'Rick'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.upload_image, name='upload_image'),
]
