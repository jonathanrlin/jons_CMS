# urls of main
from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^post/$', views.viewAllPosts),
  url(r'^post/(?P<post_id>\d+)/$', views.viewOnePost),
]