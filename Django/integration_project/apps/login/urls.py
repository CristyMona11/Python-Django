from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^authorize$', authorize, name='authorize'),
    url(r'^login$', login, name='login'),
    url(r'^success$', success, name='success'),
    url(r'^logout$', logout, name='logout')
]
