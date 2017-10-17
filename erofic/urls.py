from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^generator/', views.index),
    url(r'^home/$', views.homepage, name="Homepage"),
]
