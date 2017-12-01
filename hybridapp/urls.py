from django.conf.urls import include, url
from . import views

app_name = 'hybridapp'

urlpatterns = [
    url(r'^$', views.home, name='main'),
    url(r'^home/$', views.home, name='home'),
    url(r'^new/$', views.new, name='new'),
    url(r'^success/$', views.success, name='success'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^projectbids/(?P<project_id>\d+)', views.projectbids, name='projectbids'),
    url(r'^logout/$', views.logout, name='logout')
]
