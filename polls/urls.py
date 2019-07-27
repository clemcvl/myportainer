from django.conf.urls import url, include
#from django.urls import path
from . import views

urlpatterns = [
    url('home', views.index, name='home'),
    url('aaaaa', views.index, name='index'),
    url('toto', views.toto, name='toto'),
    url('switch', views.switch, name='switch'),
    url('name', views.nametest, name='nameform'),

]
