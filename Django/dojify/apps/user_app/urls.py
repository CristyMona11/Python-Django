from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^register$', register, name='register'),
    url(r'^login$', login, name='login'),
    url(r'^profile$', profile, name='profile'),
    url(r'^edit$', edit, name='edit'),
    url(r'^update$', update, name='update'),
    url(r'^follower$', follower, name='follower'),
    url(r'^follow/(?P<follower_id>\d+)/(?P<followee_id>\d+)$', follow, name='follow'),
    url(r'^unfollow/(?P<follower_id>\d+)/(?P<followee_id>\d+)$', unfollow, name='unfollow'),
    url(r'^logout$', logout, name='logout'),
]
