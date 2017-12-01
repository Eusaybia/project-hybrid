from django.conf.urls import include, url
from . import views

app_name = 'hybridapp'

urlpatterns = [
    url(r'^$', views.home, name='main'),
    url(r'^home/$', views.home, name='home'),
    url(r'^new/$', views.new, name='new'),
    url(r'^success/$', views.success, name='success'),
]
