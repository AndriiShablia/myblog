from django.conf.urls import url,include
from . import views

app_name='articles'
urlpatterns=[
    url(r'^$', views.HomeView, name='home'),
    url(r'^(?P<slug>\w+)/$', views.post_detail, name='detail'),
    ]