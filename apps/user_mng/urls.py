# urls of user_mng
from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.viewAllUsers),
  url(r'^(?P<user_id>\d+)/$', views.viewDetailUser),
  url(r'^new/$', views.viewAddUser),
  url(r'^addUser/$', views.conAddUser),
  url(r'^edit/(?P<user_id>\d+)/$', views.viewEditUser),
  url(r'^editUser/$', views.conEditUser),
  url(r'^delUser/$', views.conDelUser),
]