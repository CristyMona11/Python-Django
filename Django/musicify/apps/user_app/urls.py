from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^authenticate$', authenticate, name='authenticate'),
    url(r'^register$', register, name='register'),
    url(r'^profile$', profile, name='profile'),
    url(r'^edit$', edit, name='edit'),
    url(r'^logout$', logout, name='logout')
]
