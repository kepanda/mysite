from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'userinfo', views.index),
    url(r'article/(?P<y>\w{4})/$', views.article),
]