from django.conf.urls import url
from  . import views

urlpatterns = [
    url(r'followers/$', views.get_followers, name='followers'),
    url(r'$',views.follower_page,name='home')
]