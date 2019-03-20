from django.conf.urls import url
from  . import views

urlpatterns = [
    url(r'followers/$', views.get_followers, name='followers'),
]