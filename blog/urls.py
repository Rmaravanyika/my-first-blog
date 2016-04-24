from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post_list/', views.post_list, name='post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^gallery/', views.gallery, name='gallery'),
]