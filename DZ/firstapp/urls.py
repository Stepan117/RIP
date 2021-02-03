from django.urls import path
from numpy.core import generic

from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^DB/$', views.DB.as_view(), name='DB'),
]



