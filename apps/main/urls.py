from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^home$', views.home),
    url(r'^validate/reg$', views.register),
    url(r'^validate/log$', views.login),
    url(r'^book/(?P<book_id>[0-9]+)$', views.show),
    url(r'^book/(?P<book_id>[0-9]+)/edit$', views.edit),
    url(r'^book/(?P<book_id>[0-9]+)/update$', views.update),
    url(r'^book/(?P<book_id>[0-9]+)/delete$', views.delete),
]