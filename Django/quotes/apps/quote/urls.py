from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name= 'home'),
    url(r'^quote_home$', quote_home, name='quote_home'),
    url(r'^add_quote$', add_quote, name='add_quote'),
    url(r'^add_fave$', add_fave, name='add_fave'),
    url(r'^view_user$', view_user, name='view_user'),
    url(r'^logout$', logout, name='logout'),
]
