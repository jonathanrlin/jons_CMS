# urls of post_mng
from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.viewAllPosts),
  url(r'^new/$', views.viewAddPost),
  url(r'^edit/(?P<post_id>\d+)/$', views.viewEditPost),
  url(r'^addPost/$', views.conAddPost),
  url(r'^editPost/$', views.conEditPost),
  url(r'^delPost/$', views.conDelPost),
]