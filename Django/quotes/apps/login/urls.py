from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^register_user$', register, name='register'),
    url(r'^logout$', logout, name='logout'),
    url(r'^auth$', authenticate, name='authenticate'),
]