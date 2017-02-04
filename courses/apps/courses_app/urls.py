from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.add),
    url(r'^edit/(?P<course_id>\d+)$', views.edit),
    url(r'^destroy/(?P<course_id>\d+)$', views.destroy),
]
