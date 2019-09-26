# urls of log_reg
from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^admin/$', views.viewAdminLogin),
  url(r'^adminLogin_api/$', views.conAdminLogin),
  url(r'^user/$', views.viewUserLogin),
  url(r'^userLogin_api/$', views.conUserLogin),
  url(r'^logout_api/$', views.conLogout),
  url(r'^register/$', views.viewRegister),
  url(r'^addUser/$', views.conRegister),
]